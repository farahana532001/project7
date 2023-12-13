from django.shortcuts import render

# Create your views here.


def munnabhai(request):
    return render(request,'munnabhai.html')


def gudboy(request):
    return render(request,'gudboy.html')