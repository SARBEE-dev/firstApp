from django.contrib import admin
from .models import Todo
# Register your models here.
admin.site.register(Todo)
admin.site.site_header = 'TODO APP'
admin.site.site_title = 'TODO Admin Area'
admin.site.index_title = 'Welcome to the TODO APP admin area'