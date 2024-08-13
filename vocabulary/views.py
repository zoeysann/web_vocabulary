from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'vocabulary/index.html')

def info(requst):
    return HttpResponse("Hello there! This's info page.")

def quiz(request):
    return HttpResponse('This is quiz page.')
