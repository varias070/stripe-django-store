from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('buy/<int:item_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('item/<int:pk>/', views.ItemView.as_view(), name='show_item'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('create_order', views.OrderView.as_view(), name='create_order'),
    path('show_order/<int:pk>/', views.OrderView.as_view(), name='show_order'),
    path('order/buy/<int:order_id>/', views.create_checkout_session_for_order, name='create_checkout_session_for_order')
]
