from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['Lastname']
        email = request.POST['email']
        password = request.POST['password1']
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                        password=password)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'register.html')
