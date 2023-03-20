from django.shortcuts import render,HttpResponse,redirect
from .forms import SignUp
from django.contrib.auth import authenticate,login

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignUp()
    return render(request,'signup.html',{'form':form})
        

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect('next')
    else:
        return render(request,'login.html')
    

def next(request):
    return render(request,'next.html')
