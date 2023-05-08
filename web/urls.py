from . import views
from django.urls import path

app_name='web'

urlpatterns=[
    path("",views.index,name="index"),
    path("blog",views.blog,name="blog"),
    path("shop",views.shop,name="shop"),
    path("contact",views.contact,name="contact"),
    path("cart",views.cart,name="cart"),
    path("about",views.about,name="about"),
    path("checkoutt",views.checkout,name="checkout"),
    path("login",views.login,name="login"),
    path("wishlist",views.wishlist,name="wishlist"),
    path('single-product/<int:id>/', views.single_product,name='single_product'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),




    path("error",views.error,name="error"),
] 

