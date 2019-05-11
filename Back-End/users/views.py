from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from nodes.models import Division

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST["password1"])
        user.save()
        user.userprofile.monthly_budget = request.POST['budget']
        user.userprofile.energy_plan = request.POST['energy_plan']
        user.save()
        user.userprofile.save()
        login(request, user)
        return redirect('create_division')
    else:
        # return HttpResponse('Get method not allowed')
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def create_division(request):
    if request.method =='POST':
        division = Division(name = request.POST['name'])
        division.save()
        user = request.user
        user.userprofile.divisions.add(division)
        user.save()
<<<<<<< HEAD
        return redirect('nodes/register_plug')
    else:
        return render(request, 'users/create_division.html')

def login(request):
=======
        return redirect('register_plug')
    else:
        return render(request, 'users/create_division.html')

def login_view(request):
>>>>>>> master
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        authenticated = authenticate(username=user.username, password=password)
        if authenticated is not None:
            login(request, user)
        else:
            return HttpResponse('Error logging in')
<<<<<<< HEAD
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
=======
        return redirect('user_page')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


def user_page(request):
    user = request.user
    divisions = user.userprofile.divisions.all()
    return render(request, 'users/user_page.html', {'divisions': divisions})
>>>>>>> master
