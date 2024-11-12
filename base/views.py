from django.shortcuts import render
from django.http import HttpResponse




# these are the html links to the navbar about, support and safety.

def about(request):
    return render(request,'navbar_links/about.html')
def safety(request):
    return render(request,'navbar_links/safety.html')
def support(request):
    return render(request,'navbar_links/support.html')
def login(request):
    return render(request,'navbar_links/login.html')


#These are the main webpages of the studybud
def home(request):
    return render(request,'home.html')

def room(request):
    return render(request,'room.html')


