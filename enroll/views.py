from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
# Sign up
def sign_up(request):
    if request.method == 'POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully!!')
            fm.save()
            fm=SignupForm()
    else:
        fm=SignupForm()
    return render(request,'enroll/signup.html',{'form':fm})
# login form
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in succesfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()

        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


#def profile
def profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
def user_logout(request):
        logout(request)
        return HttpResponseRedirect('/login/')
