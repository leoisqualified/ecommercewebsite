from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CreateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import *

def signUpPage(request):
	form = CreateForm()

	if request.method == 'POST':
		form = CreateForm(request.POST)

	if form.is_valid():
		form.save()
		messages.success(request,'Account Created')
		return redirect('login')
	
	context = {'form': form}
	return render(request,'registration/signup.html',context)

def signInPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong Username or Password')
    
    context = {}
    return render(request, 'registration/signin.html', context)


def SignOutPage(request):
	logout(request)
	return redirect('signin')

def homePage(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkoutPage(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		item = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
		
	context	= {'items':items, 'order':order} 
	return render(request,'store/checkout.html')

def updateItem(request):
	return JsonResponse('item was added', safe=False) 




