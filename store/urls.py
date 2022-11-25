from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('buy/<int:item_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('item/<int:item_id>/', views.show_item, name='show_item'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('create_order', views.create_order, name='create_order'),
    path('show_order/<int:order_id>/', views.show_order, name='show_order'),
    path('order/buy/<int:order_id>/', views.create_checkout_session_for_order, name='create_checkout_session_for_order')
]
