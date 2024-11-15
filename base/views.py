from django.shortcuts import render
from django.http import HttpResponse
from.models import Room

#rooms = [
    #{'id':1,'name': 'resume help'},
    #{'id':2,'name': 'coding help'},
    #{'id':3,'name': 'web dev help'},
#]

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
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'base/home.html',context )

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html', context)


