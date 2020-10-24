from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('home/', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
]
