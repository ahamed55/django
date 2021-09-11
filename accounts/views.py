from django import forms
from accounts.models import Customer, Order, Product
from django.shortcuts import render,redirect
from .forms import OrderForm

# Create your views here.
def home(request):
    cust=Customer.objects.all()
    order=Order.objects.all()

    total_orders=len(order)
    delivered=len(order.filter(status='Delivered'))
    pending=len(order.filter(status='pending'))

    context={'customer':cust,'order':order,'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request,"accounts/dashboard.html",context)


def products(request):
    prod=Product.objects.all()
    return render(request,"accounts/products.html",{'products':prod})


def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    order=customer.order_set.all()
    total_order=len(order)
    context={'cus':customer,'order':order,'total_order':total_order}
    return render(request,"accounts/customer.html",context)

def order_form(request):

    form = OrderForm()
    if request.method == 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,"accounts/order_form.html",context)

def update_form(request,pk):

    order=Order.objects.get(id=pk)
    form= OrderForm(instance=order)
    if request.method == 'POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,"accounts/order_form.html",context)

def delete_order(request,pk):
    item=Order.objects.get(id=pk)
    context={'item':item}
    if request.method=="POST":
        item.delete()
        return redirect('/')
        
    return render(request,"accounts/delete_order.html",context)