from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product,Customer
from . forms import CustomerRegisterationForm,CustomerProfileForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "dairy/home.html")

def about(request):
    return render(request, "dairy/about.html")

def contact(request):
    return render(request, "dairy/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"dairy/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"dairy/category.html",locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk) 
        return render(request,"dairy/productdetail.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegisterationForm()
        return render(request,'dairy/customerregistration.html',locals())
    def post(self,request):
        form=CustomerRegisterationForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request,"User Registration Successfull")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'dairy/customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'dairy/profile.html',locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
             user=request.user
             name=form.cleaned_data['name']
             locality=form.cleaned_data['locality']
             city=form.cleaned_data['city']
             mobile=form.cleaned_data['mobile']
             state=form.cleaned_data['state']
             zipcode=form.cleaned_data['zipcode']
             
             reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
             reg.save()
             messages.success(request,"User Registration Successfull")
        else:
             messages.warning(request,"Invalid Input Data")
        return render(request,'dairy/customerregistration.html',locals())
        return render(request,'dairy/profile.html',locals())
    
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'dairy/address.html',locals())