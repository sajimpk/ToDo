from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    list1 = todo_list.objects.all()
    return render(request,'home.html',locals())

def to_list(request):
    if request.method=="POST":
        todo = request.POST.get('todo')
        if todo:
            _list= todo_list.objects.create(todo=todo)
            _list.save()
            return redirect('home')
    return render(request,'index.html',locals())

def delete(request,id):
    do = todo_list.objects.get(id=id)
    print(do)
    do.delete()
    return redirect('home')
    