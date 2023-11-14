from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['Lastname']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save()
                print('user created')
                messages.info(request, 'successfully created')
        else:
            print('password not match')
            messages.info(request, 'password not match reenter...!')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
