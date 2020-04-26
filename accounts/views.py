from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import Customer
from .decorators import unauthenticated_user, allowed_users
from .forms import CreateUserForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# Create your views here.


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was create for ' + username)
            return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'account/login.html')


def logout_user(request):
    logout(request)
    return redirect('account:login')


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['customer'])
def user_page(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    print("orders: ", orders)
    context = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        "pending": pending
    }
    return render(request, 'account/user-page.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['customer'])
def setting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'account/setting.html', context)


