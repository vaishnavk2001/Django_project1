from django.shortcuts import render
from . models import place,news


# Create your views here.
def fun(request):
    obj = place.objects.all()
    obj2 = news.objects.all()
    return render(request, 'index.html', {'result': obj,'news':obj2})
