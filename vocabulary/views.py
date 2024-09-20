from django.shortcuts import render
from django.http import HttpResponse
from .models import idk_name

# Create your views here.
def home(request):
    print('AAAAA')
    items = idk_name.objects.all()  # Retrieve all items from the database
    print('5')
    context = {
        'items': items
    }
    print(context)
    return render(request, 'vocabulary/index.html', context)

# def home(request):
#     return render(request, 'vocabulary/index.html')

def info(requst):
    return HttpResponse("Hello there! This's info page.")

def quiz(request):
    return HttpResponse('This is quiz page.')
