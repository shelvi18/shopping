from django.shortcuts import render,redirect
from . models import Product
from . forms import ProductForm
def index(request):
    item=Product.objects.all()
    return render(request,"index.html",{"item":item})
def add(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("index")
    return render(request,"add.html",{'form':form})