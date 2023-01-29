from email import message
import imp
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ese import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(username = username):
            messages.error(request, "Username already exist, Please try other Username!!!")
            return redirect('home')
         
        if User.objects.filter(email = email):
            messages.error(request, "This Email is already Registered")
            return redirect('home')

        if len(username)<5:
            messages.error(request, "username must be 5 characters!!!")
            return redirect('home')

        if password != cpassword:
            messages.error(request, "Password doesn't match!")
            return redirect('home')

        # if not username.isalnum:
        #     messages.error(request, 'username must be alphanumeric')
        #     return redirect('home')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.email = email

        myuser.save()
        messages.success(request,"Your account has been succesfully created")

        #Welcome Email
        subject = "Welcome to e-Electrical Services"
        
        message = "Hello " + myuser.first_name + "!!\n" + "\nThank you for visiting our website we will help you in every possible work like:\n-Laying wires\n-Ceiling Light Fittings\n-Switch Boards\nand many more.... \n\nThanks-\tTeam e-Electrical Services"
        
        # from_email = 'theaspire2021@gmail.com'
        # to_list = [myuser.email]

        send_mail(subject,message,'eelectricalservices22@gmail.com',[myuser.email],fail_silently=False)
        print(send_mail)
        return redirect("signin")

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username =username, password = password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"authentication/index.html", {'fname': fname} )

        else:
            messages.error(request, ' Bad Credentials')
            return redirect("home")

    return render(request,"authentication/signin.html" )

def signout(request):
    logout(request)
    messages.success(request, 'your account has successfully logged out')
    return redirect('home')

# def dltacc(request):
#     if u == User.objects.get(username = username):
#         u.delete()
#         message.success(request,"the user is deleted")
#     return redirect('home')
