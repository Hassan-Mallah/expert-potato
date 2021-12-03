from django.shortcuts import render, HttpResponse
from PyDictionary import PyDictionary


# Create your views here.

def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    dict = PyDictionary()
    meaning = dict.meaning(search)
    sysnonms = dict.synonym(search)

    print(meaning, sysnonms)

    return HttpResponse(str(meaning))
    # return render(request, 'word.html')
