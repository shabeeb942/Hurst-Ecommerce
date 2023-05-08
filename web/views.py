from django.shortcuts import render,redirect
from .models import Contact,Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# Create your views here.

def index(request):
    context={}
    return render(request,'web/index.html',context)

def blog(request):
    context={}
    return render(request,'web/blog.html',context)

def shop(request):
    context={
        'product':Product.objects.all(),
    }
    return render(request,'web/shop.html',context)

def contact(request):
    context={}
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        form =Contact(name=name , email=email, comment=comment)
        form.save()
        return redirect('web:contact')

    return render(request,'web/contact.html',context)


def about(request):
    context={}
    return render(request,'web/about.html',context)


def checkout(request):
    context={}
    return render(request,'web/checkout.html',context)


def login(request):
    context={}
    return render(request,'web/login.html',context)

def wishlist(request):
    context={}
    return render(request,'web/wishlist.html',context)

def error(request):
    context={}
    return render(request,'web/404.html',context)

def single_product(request,id):
    product=Product.objects.get(id=id)
    context = {"is_shop":True,"product":product}
    return render(request,'web/single-product.html',context)


def cart(request):
    context={}
    return render(request,'web/cart_detail.html',context)

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'web/cart_detail.html')