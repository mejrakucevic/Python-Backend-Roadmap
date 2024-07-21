from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList
# Create your views here.

def todolist(request):
    
    allTasks = TaskList.objects.all
    
    return render(request, 'todolist.html', {'allTasks': allTasks})
    
    
    
    context = {
        'welcomeText': "welcome to TaskMate"
    }
    return render(request, 'todolist.html', context)


# def contact(request):
#     context = {
#         'welcomeText': "welcome to Contact page"
#     }
#     return render(request, 'contact.html', context)