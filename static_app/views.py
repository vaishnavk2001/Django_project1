from django.shortcuts import render
from . models import place


# Create your views here.
def fun(request):
    obj = place()
    obj.name = 'kerala'
    obj.price = 600
    obj.desc = 'this is kerala'
    return render(request, 'index.html', {'result': obj})
