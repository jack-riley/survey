from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random(request):
    context = {
        'word': get_random_string(length=14),
        }
    if request.method == "POST":
        request.session['counter'] += 1
    return render (request, "random.html", context)

def reset(request):
    if request.method == "POST":
        request.session.flush() 
        request.session['counter'] = 1

    return redirect('/random_word')




# Create your views here.
