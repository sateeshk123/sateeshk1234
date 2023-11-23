"""eventmgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from eventapp import views

urlpatterns = [
    path('',views.homepage),
    path('login/',views.loginpage),
    path('register/',views.registerpage),
    path('fooditems/',views.fooditempages),
    path('logout/',views.logout),
    path('events/',views.eventspage),
    path('events/<int:eventid>',views.eventdetails),
    path('bookings/',views.myevents),
    path('bookings/<int:bid>',views.bookingdetails),
    path('additem/',views.addItemtoBooking),
    path('updatestatus/',views.updateBookingStatus),
    path('updateamount/',views.updateamount),
    path('payment/',views.payment),
    path('delitem/',views.deleteItemfromBooking),
    path('updateprogress/',views.updateprogress),
    path('admin/', admin.site.urls),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)