from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def adminlogin(request):
    if request.method=='POST':
        sid=request.POST['sid']
        pswd=request.POST['password']
        staff=Staff.objects.filter(staffid=sid,password=pswd).exists()
        if staff:
            return redirect("clothadmin:sdashboard")
    return render(request,'clothadmin/login.html')


def viewproducts(request):
    pdt=Product.objects.all()
    return render(request,'clothadmin/viewproducts.html',{'pdt':pdt})


def addproducts(request):
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        price=request.POST['price']
        category=request.POST['category']
        image=request.FILES['image']
        pdt=Product(title=title,description=description,price=price,image=image)
        pdt.save()
    return render(request,'clothadmin/addproducts.html')

def deleteproduct(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect('clothadmin:viewpdt')

def sdashboard(request):
    return render(request,'clothadmin/stdashboard.html')

def addstaffs(request):
    if request.method=='POST':
        name=request.POST['name']
        staffid=request.POST['staffid']
        password=request.POST['password']   
        staff=Staff(name=name,staffid=staffid,password=password)
        staff.save()
    return render(request,'clothadmin/addstaffs.html')

def updateproduct(request,pid):
    pdt=Product.objects.get(id=pid)
    if request.method=='POST':
        title=request.POST['title']
        description=request.POST['description']
        price=request.POST['price']
        pdt.title=title
        pdt.description=description
        pdt.price=price
        
        pdt.save()
        return redirect("clothadmin:viewpdt")
    return render(request,"clothadmin/update.html",{'product':pdt})

def update(request):
    return render(request,'clothadmin/update.html')

def viewstaffs(request):
    staff=Staff.objects.all()
    return render(request,'clothadmin/viewstaffs.html',{'staff':staff})

def deletestaff(request,sid):
    Staff.objects.get(id=sid).delete()
    return redirect('clothadmin:viewstaffs')