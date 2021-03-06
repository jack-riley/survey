from django.shortcuts import render, redirect

# Create your views here.

def results (request) :
     if request.method == "POST":
         request.session['first_name'] = request.POST['first_name'],
         request.session['last_name'] = request.POST["last_name"],
         request.session['email'] = request.POST["email"],
         request.session['location'] = request.POST["location"],
         request.session['language'] = request.POST["language"],
         request.session['comment'] = request.POST["comment"],
         request.session['counter'] = 100,
          
     return redirect('/display')

def display (request):
    return render(request, "result.html")
	
 
def form (request):
    return render(request, "request.html")
