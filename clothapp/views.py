from django.shortcuts import render,redirect
from.models import *
from clothadmin.models import *


# Create your views here.
def indexhome(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            cust=Customer.objects.get(email=email,password=password)
            request.session['customer']=cust.id
            return redirect('clothapp:dashboard')
            
        except Customer.DoesNotExist:
            return render(request,'clothapp/login.html',{'msg':'invalid username or password'})
        # if Customer.objects.filter(email=email,password=password).exists():
        #     return redirect('clothapp:dashboard')
        # else:
        #     return render(request,'clothapp/login.html',{'msg':'invalid username or password'})


    return render(request,'clothapp/login.html')

def signin(request):
    if request.method=='POST':
        name=request.POST ["name"]
        dob=request.POST ["dob"]
        email=request.POST ["email"]
        mob=request.POST ["mob"]
        state=request.POST["state"]
        address=request.POST ["address"]
        pincode=request.POST ["pincode"]
        password=request.POST ["password"]
        landmark=request.POST ["landmark"]
        customer=Customer(name=name,dob=dob,email=email,mob=mob,state=state,address=address,pincode=pincode,password=password,landmark=landmark)
        customer.save()
        return redirect("clothapp:login")
    return render(request,'clothapp/signin.html')

def home(request):
    return render (request,'clothapp/home.html')

def contactus(request):
  if 'customer' in request.session:
    if request.method=='POST':
        name=request.POST ["name"]
        email=request.POST ["email"]
        message=request.POST ["message"]
        
        cont=Contactus(name=name,email=email,message=message)
        cont.save()
       
    
    return render(request,'clothapp/contactus.html')
  else:
        return render(request,'clothapp/home.html')

def Dashboard(request):
    if 'customer' in request.session:
        return render(request,'clothapp/dashboard.html')
    else:
        return render(request,'clothapp/home.html')

def forgetpassword(request):
    return render(request,'clothapp/forgetpassword.html')

def addtocart(request):
  if 'customer' in request.session: 
        
    cart_items=Cart.objects.all()
    total_price=sum(item.product.price * item.quantity  for item in cart_items)
    total_price_per_item=[]
    grand_total=0

    for item in cart_items:
        item_total=item.product.price * item.quantity
       
        total_price_per_item.append({'item': item,'total':item_total})
        grand_total += item_total
    return render(request,'clothapp/addtocart.html', {'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
  else:
        return render(request,'clothapp/home.html')

def remove_from_cart(request,product_id):
  if 'customer' in request.session:  
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        cart_item=Cart.objects.get(product=product)
        cart_item.delete()
    return redirect('clothapp:addtocart') 
  else:
        return render(request,'clothapp/home.html')   


def dresses(request):
  if 'customer' in request.session:  
    cat=Category.objects.get(name='Dresses')
    pdts=Product.objects.filter(category=cat)

    return render(request,'clothapp/dresses.html',{'product':pdts})
  else:
        return render(request,'clothapp/home.html')

def sizechart(request):
    return render(request,'clothapp/sizechart.html')

def accessories(request):
   if 'customer' in request.session: 
    cat=Category.objects.get(name='Accessories')
    pdts=Product.objects.filter(category=cat)
    return render(request,'clothapp/accessories.html',{'product':pdts})
   else:
        return render(request,'clothapp/home.html')
    

def bags(request):
  if 'customer' in request.session:
    cat=Category.objects.get(name='Bags')
    pdts=Product.objects.filter(category=cat)
    return render(request,'clothapp/bags.html',{'product':pdts})
  else:
        return render(request,'clothapp/home.html')

def add_to_cart(request,product_id):
  if 'customer' in request.session:  
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('clothapp:addtocart')    
  else:
        return render(request,'clothapp/home.html')    

def payment(request):
    return render(request,'clothapp/payment.html')
    
def logOut(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('clothapp:home')


