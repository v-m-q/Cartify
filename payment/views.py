from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from payment.models import UserPayment
import stripe
import time


# @permission_classes([IsAuthenticated])
def purchase(request):
	# cart_id = request.data.get('cart_id')
	stripe.api_key = 'secret_key'
	price = stripe.Price.create(
				unit_amount=int(99 * 100),  # order total price in cents
				currency='usd',  
    		product='app_key',  
	)
	if request.method == 'POST':
		checkout_session = stripe.checkout.Session.create(
			payment_method_types = ['card'],
			line_items = [
				{
					'price': price,
					'quantity': 1,
				},
			],
			mode = 'payment',
			customer_creation = 'always',
			success_url = 'http://127.0.0.1:8000/pay/product_page' ,#+ '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
			cancel_url = 'http://127.0.0.1:8000' + '/payment_cancelled',
		)
		return redirect(checkout_session.url, code=303)
	return render(request, 'user_payment/product_page.html')


## use Stripe dummy card: 4242 4242 4242 4242
def payment_successful(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	checkout_session_id = request.GET.get('session_id', None)
	session = stripe.checkout.Session.retrieve(checkout_session_id)
	customer = stripe.Customer.retrieve(session.customer)
	user_id = request.user.user_id
	user_payment = UserPayment.objects.get(app_user=user_id)
	user_payment.stripe_checkout_id = checkout_session_id
	user_payment.save()
	return render(request, 'user_payment/payment_successful.html', {'customer': customer})


def payment_cancelled(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	return render(request, 'user_payment/payment_cancelled.html')


@csrf_exempt
def stripe_webhook(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	time.sleep(10)
	payload = request.body
	signature_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None
	try:
		event = stripe.Webhook.construct_event(
			payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
		)
	except ValueError as e:
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		return HttpResponse(status=400)
	if event['type'] == 'checkout.session.completed':
		session = event['data']['object']
		session_id = session.get('id', None)
		time.sleep(15)
		user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
		user_payment.payment_bool = True
		user_payment.save()
	return HttpResponse(status=200)
