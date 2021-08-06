from django.db import models
from tastypie.resources import ModelResource
from Todo_app.models import Todo
# Create your models here.

class TodoResource(ModelResource):
    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todo'