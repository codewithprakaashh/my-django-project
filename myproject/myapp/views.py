from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

# Create a view for the counter page
def counter(request):
    words = request.POST['words']
    word_count = len(words.split())
    context = {
        "words": words,
        'word_count': word_count,
    }
    return render(request, "counter.html", context)