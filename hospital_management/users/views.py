from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import *

def home_page(request):
   if not request.user.is_authenticated:
         return HttpResponseRedirect(reverse("login"))
   return render(request,"users/home_page.html")

def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect(reverse("home_page"))
        else:
            return render(request,"users/login.html")
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html")  

doctor=Doctor.objects.all()
def doctors(request):
    if request.method == "POST":
        speciality = request.POST["speciality"]
        a=list()
        for doctors in doctor:
            if doctors.department == speciality:
                a.append(doctors)
        return render(request,"users/doctors.html",{"doctor":a,"departments":departments})
    return render(request,"users/doctors.html",{"doctor":doctor,"departments":departments})

def profile(request):
    return render(request,"users/profile.html")

def appointment(request):
    appointments=Appointments.objects.all()
    user = User.objects.get(username=request.user)
    patient=user.patient
    appointments=patient.appointments
    context={"appointments":appointments,"patient":patient}
    return render(request,"users/appointment.html",context=context)