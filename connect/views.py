from django.shortcuts import render,redirect,get_object_or_404
from .forms import OrderForm,ProductForm
from .models import Order,Product,Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger




def product(request, cat_slug=None):
    cats = Category.objects.all()        
    if cat_slug:
        cat = get_object_or_404(Category,slug = cat_slug)
        products = Product.objects.filter(category = cat)
    else:
        products = Product.objects.all()
    
    paginator = Paginator(products,4)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        product_detail = paginator.page(paginator.num_pages)
    
    return render(request,"main/product.html",{"products":products})




# def product(request, cat_slug=None):
#     q = request.GET.get('q')    
#     cats = Category.objects.all()  
#     if cat_slug:
#         cat = get_object_or_404(Category,slug=cat_slug)
#         products = Product.objects.filter(category = cat)
#     elif q:
#         products= Product.objects.filter(
#         Q(title_icontains=q) | Q(description_icontains=q)
#         )
#     else:
#         products = Product.objects.all()
#     return render(request,"main/product.html",{"products":products},{"cats": cats})

@login_required(login_url="/users/login/")
def add_product(request):
    form = ProductForm
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    return render(request,"main/add_product.html",{"form":form})


@login_required(login_url="/users/login/")
def add_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():  
                                 
            Order.objects.create(
                
                customer=form.cleaned_data.get('customer'),
                total_price=form.cleaned_data.get('total_price'),
                products=form.cleaned_data.get('products')
                )         
            return redirect("orderlist")
    return render(request, "main/add_order.html",{"form": form})




def orderlist(request):
    order = Order.objects.all()    
    return render(request, "main/orderlist.html",{"orders":order})

@login_required(login_url="/users/login/")
def delete_order(request,customer):
    order =Order.objects.get(customer)
    print(order[0])
    order.delete()
    return redirect('connect/orderlist')


def product_detail(request,pk):
    product =get_object_or_404(Product,id=pk)
    return render(request,"main/product_detail.html", {"product": product})

