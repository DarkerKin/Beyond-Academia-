from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
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


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request,'base/room_form.html',context )


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
  
    context = {'form': form}
    return render(request,'base/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
  

    return render(request,'base/delete.html',{'obj':room})
