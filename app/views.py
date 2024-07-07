from django.shortcuts import render  
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TodoList
from django.urls import reverse_lazy

class List(ListView):
    model = TodoList
    template_name = 'list.html'
    context_object_name = 'todos'
    
class Detail(DetailView):
    model = TodoList
    template_name = 'detail.html'
    context_object_name = 'todo'
    pk_url_kwarg = 'id'
    
class Create(CreateView):
    model = TodoList
    template_name = 'create.html'
    fields = ['title', 'description', 'status', 'deadline']
    success_url = reverse_lazy('list')

class Update(UpdateView):
    model = TodoList
    template_name = 'update.html'
    fields = ['title', 'description', 'status', 'deadline']
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('list')
    
    
class Delete(DeleteView):
    model = TodoList
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('list')
    context_object_name = 'todo'