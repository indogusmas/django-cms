from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, Customer

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customer = customers.count()
    _filter_delivery = {'status':'Delivery'}
    delivered = orders.filter(**_filter_delivery).count()
    _filter_pending = {'status':'Pending'}
    pending = orders.filter(**_filter_pending).count()

    context = {'orders':orders, 'customers':customers,'total_customers':total_customer,
                'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders =  customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'accounts/customers.html',context)
