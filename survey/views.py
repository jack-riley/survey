from django.shortcuts import render, redirect

# Create your views here.

def results (request) :
     if request.method == "POST":
         context = {
         'first_name': request.POST["first_name"],
         'last_name': request.POST["last_name"],
         'email': request.POST["email"],
         'location' : request.POST["location"],
         'favorite_language': request.POST["language"],
         'first_comment' : request.POST["comment"],
          }
         return render(request, 'result.html', context)
     return render (request, 'result.html')

 
def form (request):
    return render(request, "request.html")
