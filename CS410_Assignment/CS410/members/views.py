from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import student, teach, member
# Create your views here.

def teacher(request):
    return render(request, 'members/teacher.html', {})

def teacher(request):
    return render(request, 'members/student.html', {})

@login_required
def home(request):
    return render(request, 'members/register.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        title = request.POST.get('title')
        password = request.POST.get('password')
        email="test@gmail.com"

        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Error, username already exists, User another.')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        if title == "teacher":
            new_member = teach(user=new_user)
            new_member.save()
        else:
            new_member = student(user=new_user)
            new_member.save()

        messages.success(request, 'User successfully created, login now')
        return redirect('login')
    return render(request, 'members/register.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    #if request.user.is_authenticated:
        #return redirect('home-page')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)

            try:
                title = student.objects.get(user=request.user)
            except:
                print("does not exist")

            try:
                title = teach.objects.get(user=request.user)
            except:
                print("does not exist")

            if title == 'Student':
                return redirect('student')
            else:
                return redirect('teacher')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')


    return render(request, 'members/login.html', {})
