from django.shortcuts import render
from Moviesapp.models import Moviesapp
from Moviesapp.forms import filmform


def viewmovie(request,p):
    b=Moviesapp.objects.get(id=p)
    return render(request,'view.html',{'movie':b})


def editmovie(request,p):
    b=Moviesapp.objects.get(id=p)
    form=filmform(instance=b)
    if(request.method=="POST"):
        form=filmform(request.POST,request.FILES,instance=b)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'add.html',{'form':form})

def deletemovie(request,p):
    b=Moviesapp.objects.get(id=p)
    b.delete()
    return home(request)