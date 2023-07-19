from django.shortcuts import render,redirect

from .models import Member

def index(request):
    member = Member.objects.all()
    return render(request,'app/index.html',{'member':member})


def add(request):
    return render(request,"app/add.html")

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=Member(firstName=x,lastName=y)
    member.save()
    return redirect("index")

def delete(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect("index")


def update(request,id):
    member= Member.objects.get(id=id)
    return render(request,"app/update.html",{"member":member})

def uprecord(request,id):
    x=request.POST['first']
    y=request.POST['last']
    member = Member.objects.get(id=id)
    member.firstName=x
    member.lastName=y
    member.save()
    return redirect("index")

