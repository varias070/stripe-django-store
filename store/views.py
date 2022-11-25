import stripe

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST


from .cart import Cart
from .models import Item, Order
from .forms import CartAddProductForm, OrderCreate

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
bead_list = ['[', ']', '"', "'", ',']


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
    return JsonResponse({"id": session['id']})


def create_checkout_session_for_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    session = stripe.checkout.Session.create(
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': "order",
            },
            'unit_amount': order.price,
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/',
        cancel_url=f'http://localhost:8000/show_order/{order_id}/',
    )
    return JsonResponse({"id": session['id']})


def show_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/item.html', {'item': item, 'cart_product_form': cart_product_form})


def show_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    cart = Cart(request)
    return render(request, 'store/order.html', {'order': order, 'cart': cart})


@require_POST
def create_order(request):
    cart = Cart(request)
    items = cart.__dict__['cart'].keys()
    items_ids = [i for i in items]
    order = Order(price=cart.get_total_price())
    order.save()
    for item_id in items_ids:
        order.items.add(item_id)
    order.save()
    return redirect(f"show_order/{order.id}")


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    print(item)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item, quantity=cd['quantity'])
    return redirect('store:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('store:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    form = OrderCreate()
    return render(request, 'store/cart.html', {'cart': cart, "form": form})
