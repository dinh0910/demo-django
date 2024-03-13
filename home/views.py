from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User

# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, 'pages/home.html', {'users': users})


def create(req):
    if req.method == 'POST':
        User.objects.create(
            name=req.POST.get('name'),
            age=req.POST.get('age'),
            gender=req.POST.get('gender'),
        )
        return redirect('list')
    return render(req, 'pages/create.html')


def edit(req, pk):
    user = get_object_or_404(User, pk=pk)
    if req.method == 'POST':
        user.name = req.POST.get('name')
        user.age = req.POST.get('age')
        user.gender = req.POST.get('gender')
        user.save()
        return redirect('list')
    return render(req, 'pages/edit.html', {'item': user})


def delete(req, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('list')
