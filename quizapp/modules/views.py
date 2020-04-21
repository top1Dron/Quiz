from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ModuleForm
from .models import Module
from .services import ModuleServices


services = ModuleServices()


def getSubjectAndRedirect(request, pk):
    """view to get subject id and redirect to create module"""

    services.subject = services.getSubject(subjectId=pk)[0]
    return redirect(reverse("modules:create"))


class ModuleCreate(CreateView):
    """class base view for creating new module"""


    model = Module
    form_class = ModuleForm
    template_name = 'modules/create.html'


    def form_valid(self, form):
        form.instance.subject = services.subject
        return super().form_valid(form)


class ModuleListView(ListView):
    """class base view for view list of subject modules"""

    model = Module
    context_object_name = 'modules'
    template_name = 'modules/list.html'

    
    def get_queryset(self):
        return services.getSubjectModules(self.kwargs['pk'])


class ModuleUpdate(UpdateView):
    """class based view for updating modules"""


    model = Module
    form_class = ModuleForm
    template_name = 'modules/update.html'


class ModuleDelete(DeleteView):
    """class based view for deleting modules"""
    
    model = Module
    success_url = reverse_lazy('subjects:list')
    

    def delete(self, *args, **kwargs):
        module = services.getModule(moduleId=self.kwargs['pk'])
        self.success_url = reverse_lazy('modules:get-subject-modules', kwargs={ "pk": module.subject.id })
        return super(ModuleDelete, self).delete(*args, **kwargs)