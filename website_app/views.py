
from random import randrange
from django.views import View
from django.contrib.auth.models import User
import razorpay
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from website_app.models import coffee,Cart,Order,booktable
from django.db.models import Q


# Create your views here.
def home(request):
    context={}
    c=coffee.objects.filter(is_active=True)
    context['coffee']=c
    print(c)
    return render(request,'home.html',context)
    # return render(request,"home.html")

def menu(request):
    context={}
    c=coffee.objects.filter(is_active=True)
    context['coffee']=c
    print(c)
    return render(request,'menu.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def book_table(request):
    if request.method == 'POST':
        userid=request.user.id
        name = request.POST['name']
        phoneno = request.POST['phone']
        email = request.POST['email']
        people = request.POST['people']
        message = request.POST['message']
        date = request.POST['date']
        time = request.POST['time']

        print(name,phoneno,email,people,message,date,time)
        context={}
        if name=="" or phoneno=="" or people=="" or message=="" or email=="" or date=="" or time=="" :
            context['prrmsg']="fields cannot be empty.."
            return render(request,'booktable.html',context)
        else:
            u=booktable.objects.create(name=name,phoneno=phoneno,people=people,message=message,email=email,date=date,time=time,userid=userid)           
            # u=authenticate(name=pname,phoneno=phoneno,noofcoffee=noofcoffee,address=address,email=email)           
            u.save()
            # context['success']="Your table is Booked successfully !!"
            # return render(request,'booktable.html',context)
            return redirect('/showtable')
    else:
        return render(request,'booktable.html')

def user_register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="feilds cannot be empty.."
            return render(request,'register.html',context)
        elif upass != ucpass:
            context['errmsg']="password and confirm password didn't match.."
            return render(request,'register.html',context)
        else:  
            try:  
                u = User.objects.create(username=uname, password=upass,email=uname)
                u.set_password(upass)       #encrypt format
                u.save()
                context['success']="User created successfully"
                return render(request, 'register.html',context)
            except Exception:
                context['errmsg']="user with same username already present.."
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')

    

def user_login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="fields cannot be empty.."
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u is not None:
                login(request,u)    # start the session
                return redirect('home/')
            else:
                context['errmsg']="Invalid username and password.."
                return render(request,'login.html',context)            
    else:
     return render(request,'login.html')
 
def user_logout(request):
    logout(request)
    return redirect('home/')


def catfilter(request,cv):
    if cv == "1":
        z="COLD COFFEE"
    elif cv == "2":
        z="HOT COFFEE"
    elif cv == "3":
        z="BLACK COFFEE"
    else:
        z="COFFEE HOUSE SPECIAL"
    print(z)

    q1=Q(is_active=True)
    q2=Q(cat=cv)
    c=coffee.objects.filter(q1 & q2)
    context={}
    context['coffee']=c
    context['cat']=z
    return render(request,"home.html",context)


def range(request):
    min=request.GET['min']
    max=request.GET['max']
    q1=Q(price__gte=min)
    q2=Q(price__lte=max)
    q3=Q(is_active=True)
    c=coffee.objects.filter(q1 & q2 & q3)
    context={}
    context['coffee']=c
    return render(request,"home.html",context)

def sort(request,sv):
    if sv=='0':
        col="price"  #ascending order
    else:
        col="-price"   # descending order 
    c=coffee.objects.filter(is_active=True).order_by(col)
    context={}
    context['coffee']=c
    return render(request,"home.html",context)

def coffee_details(request,cid):
    c=coffee.objects.filter(id=cid)
    context={}
    context['coffee']=c
    return render(request,"coffee_details.html",context)

def gallery(request):
    return render(request,'gallery.html')

def addtocart(request,cid):
    if request.user.is_authenticated:
        userid=request.user.id 
        u=User.objects.filter(id=userid)
        print(u[0])   # user object
        c=coffee.objects.filter(id=cid)
        print(c[0])    # coffee object
        q1=Q(uid=u[0])
        q2=Q(cid=c[0])
        c1=Cart.objects.filter(q1 & q2)
        n=len(c1)
        context={}
        context['coffee']=c
        if n==1:
            context['msg']="Coffee added successfully !!"
        else:
            c1=Cart.objects.create(uid=u[0],cid=c[0])
            c1.save()
            context['success']="Coffee added successfully !!"
        return render(request,"coffee_details.html",context)
    else:
        return redirect("/login")
    
def viewcart(request):
    c1=Cart.objects.filter(uid=request.user.id)
    s=0
    nc=len(c1)
    for x in c1:
        s=s+x.cid.price * x.qty 
    print(s)
    context={}
    context["coffee"]=c1
    context['total']=s
    context['n']=nc
    return render(request,"cart.html",context)

def remove(request,cid):
    c1=Cart.objects.filter(id=cid)
    c1.delete()
    return redirect('/viewcart')

def updateqty(request,qv,cid):
    c1=Cart.objects.filter(id=cid)
    print(c1)             #object queryset
    print(c1[0])          #object
    print(c1[0].qty)      #quantity only
    if qv == '1':
        t=c1[0].qty+1
        c1.update(qty=t)
    else:
        if c1[0].qty>1:      #1>1=F
            t=c1[0].qty-1
            c1.update(qty=t)    
    return redirect('/viewcart')

def placeorder(request):
    userid=request.user.id 
    print(userid)
    c1=Cart.objects.filter(uid=userid)
    print(c1)
    oid=randrange(1000,9999)
    print("order_id:",oid)
    for x in c1:
        # o=Order.objects.create(Order_id=oid,uid=x.uid,cid=x.cid,qty=x.qty)
        o=Order.objects.create(Order_id=oid,uid=x.uid,cid=x.cid,qty=x.qty)
        o.save()
        x.delete()  
        orders=Order.objects.filter(uid=request.user.id)
        context={}
        context['coffee']=orders
        np=len(orders)
        s=0
        for x in orders:
            s=s+x.cid.price*x.qty
        context['total']=s
        context['n']=np
    # return render(request,"placeorder.html",context)
    return render(request,"placeorder.html",context)
    
        
def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    print('orders:',orders)
    s=0
    oid = 0
    for x in orders:
        s=s+x.cid.price * x.qty
        oid=x.Order_id
        print(x)

    print(request.user.id)    
    client = razorpay.Client(auth=("rzp_test_TejwQSaMhByD1E", "TMjNlgTZtKViBf8dupDaDFZ5"))
    data = { "amount": s*100, "currency": "INR", "receipt": str(oid) }
    # data = {"amount":s*100,"currency":"INR","receipt":oid}
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['data']=payment
    for x in orders:
        # o=Order.objects.create(Order_id=oid,uid=x.uid,cid=x.cid,qty=x.qty)
        x.delete()
    return render(request,"pay.html",context)


# def makepayment(request):
#     orders=Order.objects.filter(uid=request.user.id)
#     s=0
#     for x in orders:
#         s=s+x.cid.price * x.qty
#         oid=x.Order_id
#     # client = razorpay.Client(auth=("rzp_test_TejwQSaMhByD1E", "TMjNlgTZtKViBf8dupDaDFZ5"))
#     client = razorpay.Client(auth=("rzp_test_TejwQSaMhByD1E", "TMjNlgTZtKViBf8dupDaDFZ5"))
#     data = { "amount": s*100, "currency": "INR", "receipt": oid}
#     payment = client.order.create(data=data)
#     print(payment)
#     context={}
#     context['data']=payment
#     return render(request,'pay.html',context)
#     # return HttpResponse("in make payment section.")

# def index(request):
#     return render(request,"index.html")

def showtable(request):
    z=booktable.objects.filter(userid=request.user.id)
    context={}
    print("tables",z)
    context['data']=z
    return render(request,"showtable.html",context)