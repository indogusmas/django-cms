from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.http import HttpResponse
from .models import Product, Order, Customer
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

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


def loginPage(request):
    context = {}
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or password is incorrect')
            
    
    return render(request, 'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect ('login')
    
    context = {'form':form}
    return render(request, 'accounts/register.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders =  customer.order_set.all()
    orders_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customer':customer,'orders':orders,'orders_count':orders_count,
    'myFilter':myFilter}
    return render(request,'accounts/customers.html',context)

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order,fields=('product','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        print('Printing POSt', request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'form':formset}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request,'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {
        'item':order
    }
    if request.method == "POST":
        print('delete',order)
        order.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', context)
    
    