from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def homepage(req):
    print(req.session)
    return render(req,"index.html")

def fooditempages(req):
    if req.method=="POST":
        name=req.POST.get("name")
        unit=req.POST.get("unit")
        remarks=req.POST.get("remarks")
        item=FoodItem(name=name,unit=unit,remarks=remarks)
        item.save()
        messages.success(req,"Item saved successfully")
        return redirect('/fooditems')
    items=FoodItem.objects.all()
    return render(req,"fooditems.html",locals())

def eventspage(req):
    if req.method=="POST":
        name=req.POST.get("name")
        place=req.POST.get("place")
        capacity=req.POST.get("capacity")
        photo=req.FILES.get("photo")
        event=Event(name=name,place=place,maxcapacity=capacity,photo=photo)
        event.save()
        messages.success(req,"Event saved successfully")
        return redirect("/events")
    events=Event.objects.all() 
    isadmin=req.session.get("role")=='Admin'   
    return render(req,"events.html",locals())

def eventdetails(req,eventid):
    if(req.method=="POST"):
        eventdate=req.POST.get("eventdate")
        adults=req.POST.get("adults")
        child=req.POST.get("child")
        user=User.objects.get(pk=req.session.get("userid"))
        event=Event.objects.get(pk=eventid)
        bk=Booking(event=event,book_date=eventdate,adults=adults,child=child,user=user)
        bk.save()
        messages.success(req,"Event booked successfully")
        return redirect("/bookings")    
    ev=Event.objects.get(pk=eventid)
    return render(req,"details.html",locals())

def myevents(req):
    if(req.session['role']=='Admin'):
        blist=Booking.objects.all()
    else:
        user=User.objects.get(pk=req.session.get("userid"))
        blist=Booking.objects.filter(user=user)        
    return render(req,"booking.html",locals())

def bookingdetails(req,bid):
    isuser=req.session.get("role")=='User'
    isadmin=req.session.get("role")=='Admin'
    bk=Booking.objects.get(pk=bid)
    items=FoodItem.objects.all()
    bitems=BookingItem.objects.filter(booking=bk)
    return render(req,"bookdetails.html",locals())

def updateamount(req):
    bid=req.POST.get("bid")
    amount=req.POST.get("amount")
    bk=Booking.objects.get(pk=bid)
    bk.amount=amount
    bk.status='Amount Proposed'
    bk.save()
    messages.success(req,"Amount updated successfully")
    return redirect('/bookings/'+bid)

def deleteItemfromBooking(req):
    itemid=req.GET.get("itemid")
    bid=req.GET.get("bid")
    print(itemid,bid)
    bk=BookingItem.objects.get(pk=itemid)
    bk.delete()
    messages.success(req,"Item deleted from booking")
    return redirect('/bookings/'+bid)

def updateprogress(req):
    bid=req.POST.get("bid")
    progress=req.POST.get("progress")
    bk=Booking.objects.get(pk=bid)
    bk.progress=progress
    if int(progress) >= 100:
        bk.status='Completed'
    else:
        bk.status='Under Progress'
    bk.save()
    messages.success(req,"Status updated")
    return redirect('/bookings/'+bid)

def payment(req):
    bid=req.POST.get("bid")
    cardno=req.POST.get("cardno")
    bk=Booking.objects.get(pk=bid)
    bk.cardno=cardno
    bk.status='Confirmed and Paid'
    bk.save()
    return redirect('/bookings/'+bid)

def addItemtoBooking(req):
    bid=req.POST.get("bid")
    itemid=req.POST.get("itemid")
    qty=req.POST.get("qty")
    print(locals())
    fitem=BookingItem(
        item=FoodItem.objects.get(pk=itemid),
        booking=Booking.objects.get(pk=bid),
        qty=qty
        )
    fitem.save()
    messages.success(req,"Item added to booking")
    return redirect("/bookings/"+bid)

def updateBookingStatus(req):
    status=req.GET.get("status")
    bid=req.GET.get("bid")
    bk=Booking.objects.get(pk=bid)
    bk.status=status
    bk.save()
    return redirect("/bookings/"+bid)

def logout(req):
    req.session.clear()
    return redirect('/')

def loginpage(req):
    if(req.method=='POST'):
        userid=req.POST.get("userid")
        pwd=req.POST.get("pwd")
        user=User.objects.filter(userid=userid,pwd=pwd).first()
        print(user)
        if user is not None:
            req.session["userid"]=user.userid
            req.session["uname"]=user.uname
            req.session["role"]="Admin" if user.isadmin else "User"
            return redirect('/')
        else:
            messages.error(req,"Invalid username or password")
            return redirect("/login") 
    return render(req,"login.html")

def registerpage(req):
    if req.method=="POST":
        userid=req.POST.get("userid")
        uname=req.POST.get("uname")
        pwd=req.POST.get("pwd")
        gender=req.POST.get("gender")
        phone=req.POST.get("phone")
        user=User(userid=userid,uname=uname,pwd=pwd,gender=gender,phone=phone)
        user.save()
        messages.success(req,"User registered successfully")
        return redirect('/login')
    return render(req,"register.html")

