import stripe

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST


from .cart import Cart
from .models import Item
from .forms import CartAddProductForm

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def create_checkout_session(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': item.name,
            },
            'unit_amount': item.price,
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/',
        cancel_url='http://localhost:8000/item/1/',
    )
    print(session)
    return JsonResponse({"id": session['id']})


def show_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/item.html', {'item': item, 'cart_product_form': cart_product_form})


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item, quantity=cd['quantity'])
    return redirect('store:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=product_id)
    cart.remove(item)
    return redirect('store:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return HttpResponse(cart)

