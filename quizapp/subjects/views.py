from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import SubjectForm
from .models import Subject
from .services import SubjectServices

services = SubjectServices()

class SubjectCreate(CreateView):
    """class base view for creating new subject"""


    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/create.html'


class SubjectListView(ListView):
    """class base view for view list of subjects"""

    model = Subject
    context_object_name = 'subjects'
    template_name = 'subjects/list.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class SubjectUpdate(UpdateView):
    """class based view for updating subjects"""


    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/update.html'


class SubjectDelete(DeleteView):
    """class based view for deleting subjects"""
    
    
    model = Subject
    success_url = reverse_lazy('subjects:list')