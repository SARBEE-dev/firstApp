from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo

def index(request):
    context = {
        'todo': Todo.objects.all().order_by('-added_date')
    }
    return render(request, 'index.html', context)

@csrf_exempt
def add_todo(request):
    added_time = timezone.now()
    content = request.POST["content"]
    created_objects = Todo.objects.create(added_date = added_time, text = content)
    created_objects.save()
    return redirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')
