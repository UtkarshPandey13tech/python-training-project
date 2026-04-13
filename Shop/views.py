from django.shortcuts import render, HttpResponse, redirect
from .models import Contact , Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')
def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})
def about(request): # request accepted from user and return response to user
    return render(request,'about.html')
def catlogue(request):
    products = Product.objects.all()
    return render(request, 'catlogue.html', {'products': products})
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emailid = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        c = Contact(name = name , emailid = emailid ,phone = phone , msg = msg)
        c.save()
        return redirect('/contact')
    data = Contact.objects.all()
    return render (request,'contact.html',{"data":data})
          
def loginView(request):
    if request.method =="POST":
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(username=userName, password=password)
        if user is not None:
           login(request , user)
           # A backend authenticated the credentials
           return redirect('/home')
       
        else:
           # No backend authenticated the credentials
           return render(request ,"login.html",{"error":"UserName or Password is Incorrect"})
    

    return render(request , "login.html")

def signupView(request):
     if request.method == "POST":
         firstName = request.POST.get('firstName')
         lastName = request.POST.get('lastName')
         userName = request.POST.get('userName')
         email = request.POST.get('email')
         password = request.POST.get('password')
         cpassword = request.POST.get('cpassword')
          
         if password == cpassword:
             user = User.objects.create_user(userName , email , password )
             user.first_name = firstName
             user.last_name = lastName
             user.save()
             return redirect('/login')
     return render(request , "signup.html")

def logoutView(request):
    logout(request)
    return redirect('/login')