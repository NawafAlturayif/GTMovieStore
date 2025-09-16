from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cart.models import Order, Item # Import Order and Item models
from django.db.models import Sum # Import Sum for aggregation


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})

@login_required
def subscription_level(request):
    template_data = {}
    template_data['title'] = 'Subscription Level'

    user = request.user
    total_spent = 0

    # Calculate total spending
    # Get all orders for the current user
    user_orders = Order.objects.filter(user=user)

    # Sum the total price of all items in all orders
    # This assumes Item has a 'price' and 'quantity' field
    # and that 'price' is the price at the time of purchase.
    for order in user_orders:
        for item in order.item_set.all():
            total_spent += item.price * item.quantity

    # Determine subscription tier
    if total_spent < 15:
        subscription_tier = "Basic"
    elif 15 <= total_spent < 30:
        subscription_tier = "Medium"
    else:
        subscription_tier = "Premium"

    template_data['total_spent'] = total_spent
    template_data['subscription_tier'] = subscription_tier

    return render(request, 'accounts/subscription_level.html', {'template_data': template_data})

