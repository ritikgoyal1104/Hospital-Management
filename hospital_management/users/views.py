from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime

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


def doctors(request):
    doctor=Doctor.objects.all()
    department=Departments.objects.all()
    if request.method == "POST":
        speciality = request.POST["speciality"]
        department=Departments.objects.filter(department=speciality)
        # for dept in department:
        #     if "Cardiologists" == dept.department:
        return render(request,"users/doctors.html",{"doctor":department.doctors,"departments":department})
    return render(request,"users/doctors.html",{"doctor":doctor,"departments":department})

def profile(request):
    appointments=Appointments.objects.all()
    user = User.objects.get(username=request.user)
    patient=user.patient
    context={"appointments":patient.appointments.all(),"patient":patient}
    return render(request,"users/profile.html",context=context)

def appointment(request,doctor_id):
    user = User.objects.get(username=request.user)
    patient=user.patient

    doctor = Doctor.objects.get(pk=doctor_id)
    if request.method == "POST":
        day = request.POST["day"]
        month = request.POST["month"]
        year = request.POST["year"]
        tempappointment = TempAppointment.objects.create(patient=patient.id, doctor=doctor.id, slot=f'{year}-{month}-{day}', status=False)
        tempappointment.save()
        return render(request,"users/home_page.html")
    return render(request,"users/appointment.html",{"doctor" : doctor})