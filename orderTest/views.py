from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser

from rest_framework.response import Response
from rest_framework import status

from orderTest.models import Order2
from orderTest.serializer import Order2Serializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    orders = Order2.objects.filter(cart_items__status='done').order_by('-created_at')
    # orders = Order2.objects.filter(cart_items__status='done', user=request.user).distinct()
    print(orders)
    serializer = Order2Serializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])

def order_detail(request, pk):
    try:
        order = Order2.objects.get(pk=pk)
    except Order2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_order_status(request, pk):
    try:
        order = Order2.objects.get(pk=pk)
    except Order2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    new_status = request.data.get('status')
    if new_status:
        order.status = new_status
        order.save()
        return Response({'message': 'Order status updated successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'New status not provided'}, status=status.HTTP_400_BAD_REQUEST)

