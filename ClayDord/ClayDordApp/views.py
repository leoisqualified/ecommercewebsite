from django.shortcuts import render, redirect
from .forms import CreateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

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
    return render(request,'store/store.html')

@login_required(login_url = 'signin')
def shopPage(request):
    return render(request,'shop.html')

def cartPage(request):
    return render(request,'store/cart.html')

def checkoutPage(request):
	context = {}
	return render(request,'store/checkout.html')




