from django.shortcuts import render

# Create your views here.

def home(request, id):
    context = { 'id': id }
    return render(request, 'home.html', context)