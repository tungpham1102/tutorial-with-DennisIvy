from django.shortcuts import render, redirect

from accounts.decorators import allowed_users, admin_only
from .models import *
from .forms import OrderForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers' : customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request, 'core/home.html', context)


@login_required()
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'core/products.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter,
    }
    return render(request, 'core/customer.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'formset': formset
    }
    return render(request, 'core/order_form.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'core/order_form.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'core/delete.html', context)