from django.shortcuts import render
from . models import place


# Create your views here.
def fun(request):
    obj2 = place()
    obj = place()
    obj.name = 'kerala'
    obj.price = 600
    obj.desc = 'this is kerala'
    obj2.name="tamilnadu"
    obj2.desc = 'this is tamilnadu'
    obj2.price = 500
    return render(request, 'index.html', {'result': obj,'tml':obj2})
