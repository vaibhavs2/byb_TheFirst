from cart.models import OrderItem
def number_of_item_in_cart(request):
    if request.user.is_authenticated:
        return {
            'items_inCart':OrderItem.objects.filter(user=request.user, is_ordered=False).count(),}
    else:
        return {'items_inCart':0,}
