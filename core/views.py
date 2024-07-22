from django.shortcuts import render,redirect
from item.models import *
from .forms import *
from django.contrib.auth import logout
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=SignupForm()
    return render(request,'core/signup.html',{'form':form})


def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    return render(request,'core/index.html',{'categories':categories,'items':items})

def contact(request):
    return render(request,'core/contact.html')

def Logout(request):
    logout(request)
    return redirect('/')