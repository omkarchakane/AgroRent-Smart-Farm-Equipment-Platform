from django.shortcuts import render, redirect
from .models import Equipment, RentalRequest
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    search = request.GET.get('search')
    if search:
        equipment = Equipment.objects.filter(name__icontains = search, is_available=True) #! filters equipment using icontains
    else:
        equipment = Equipment.objects.filter(is_available=True)
    return render(request,'home.html',{'equipments':equipment})     #! send equipments list to it.    

@login_required
def rent_equipment(request,id):
    equipment = Equipment.objects.get(id=id)

    if request.method =="POST":
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        d1 = date.fromisoformat(start_date)
        d2 = date.fromisoformat(end_date)

        if d2 <= d1 :
            messages.error(request,"End date must be greater than start date")
            return redirect ('rent',id=id)

        total_days = (d2-d1).days
        total_price = total_days * equipment.price_per_day

        RentalRequest.objects.create(
            user = request.user,
            equipment = equipment,
            start_date=start_date,
            end_date= end_date,
            total_days=total_days,
            total_price=total_price,
        )
        
        return redirect('history')
    return render(request, 'rent.html',{'equipment':equipment})

@login_required
def history(request):
    data = RentalRequest.objects.filter(user=request.user)
    return render(request,'history.html',{'data':data}) #! Send variable data to the template with name data.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'register.html')

def user_login(request):    #! login() creates session
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
    return render (request,'login.html')    


def user_logout(request):  #! logout() removes session
    logout(request)
    return redirect('login')
        
