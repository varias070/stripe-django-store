from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('buy/<int:item_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('item/<int:item_id>/', views.show_item, name='item'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/<int:item_id>/', views.cart_add, name='cart_add'),
    path('remove/(<int:Item_id>)/', views.cart_remove, name='cart_remove'),
]
