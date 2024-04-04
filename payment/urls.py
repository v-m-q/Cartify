from django.urls import path
from . import views

urlpatterns = [
	path('pay_page', views.purchase, name='product_page'),
	path('payment_successful', views.payment_successful, name='payment_successful'),
	path('payment_cancelled', views.payment_cancelled, name='payment_cancelled'),
	path('stripe_webhook', views.stripe_webhook, name='stripe_webhook'),
]