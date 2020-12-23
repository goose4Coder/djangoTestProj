from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import json
from .models import *
def store(request):
    if User.is_authenticated:
        customer= request.user.customer
        order,created= Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems=0
    products= Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    # return HttpResponse(Product.objects.filter(name='Project source code'))
    return render(request,'store/store.html',context)
def cart(request):
    if User.is_authenticated:
        customer= request.user.customer
        order,created= Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems=0
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)
def checkout(request):
    if User.is_authenticated:
        customer= request.user.customer
        order,created= Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems=0
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)
def home(request):
    if User.is_authenticated:
        customer= request.user.customer
        order,created= Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems=0
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/index.html',context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
