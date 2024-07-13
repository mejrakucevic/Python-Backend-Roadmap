from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todolist(request):
    context = {
        'welcomeText': "welcome to TaskMate"
    }
    return render(request, 'todolist.html', context)


def contact(request):
    context = {
        'welcomeText': "welcome to Contact page"
    }
    return render(request, 'contact.html', context)