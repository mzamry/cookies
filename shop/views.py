from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop')  # Redirect to the shop page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def shop(request):
    # Display products
    products = [
        {"name": "Chocolate Cookies", "price": 5.00, "image": "cookie.jpg", "id": 1},
        {"name": "Strawberry Cake", "price": 20.00, "image": "cake.jpg", "id": 2},
        {"name": "Blueberry Muffins", "price": 8.00, "image": "muffin.jpg", "id": 3},
    ]
    return render(request, 'shop.html', {'products': products})

def checkout(request):
    # Implement checkout logic and redirect to Worldcoin payment gateway
    if request.method == 'POST':
        # Placeholder for actual payment handling logic
        return redirect('payment_success')  # This should be the success page after payment
    return render(request, 'checkout.html')
