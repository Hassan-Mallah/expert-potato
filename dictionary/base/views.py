from django.shortcuts import render, HttpResponse
from PyDictionary import PyDictionary


# Create your views here.

def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    dict = PyDictionary()
    meaning = dict.meaning(search)
    synonyms = dict.synonym(search)
    antonyms = dict.antonym(search)
    if meaning and 'Noun' in meaning:
        meaning = meaning['Noun'][0]
    context = {
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    print(context)

    return render(request, 'word.html', context)
