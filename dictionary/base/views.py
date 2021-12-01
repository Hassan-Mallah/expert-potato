from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word(reqest):
    return render(reqest, 'word.html')