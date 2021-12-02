from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    print(search)
    return render(request, 'word.html')
