from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ModuleForm
from .models import Module
from .services import ModuleServices


services = ModuleServices()

class ModuleGetCreate(CreateView):
    """class base view for creating new module"""


    model = Module
    form_class = ModuleForm
    template_name = 'modules/create.html'


    def get(self, request, pk, *args, **kwargs):
        services.subject = services.getSubject(subjectId=pk)[0]
        return super().get(request, *args, **kwargs)


class ModuleCreate(CreateView):
    """class base view for creating new module"""


    model = Module
    form_class = ModuleForm
    template_name = 'modules/create.html'


    def form_valid(self, form):
        form.instance.subject = services.subject
        return super().form_valid(form)


class ModuleListView(ListView):
    """class base view for view list of subjects"""

    model = Module
    context_object_name = 'modules'
    template_name = 'modules/list.html'

    
    def get_queryset(self):
        return services.getSubjectModules(self.kwargs['pk'])

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ModuleUpdate(UpdateView):
    """class based view for updating subjects"""


    model = Module
    form_class = ModuleForm
    template_name = 'subjects/update.html'


class ModuleDelete(DeleteView):
    """class based view for deleting subjects"""
    
    
    model = Module
    success_url = reverse_lazy('subjects:list')
