from django.urls import path
from . import views


app_name = 'modules'


urlpatterns = [
    path('get-subject-modules/<int:pk>', views.ModuleListView.as_view(), name='get-subject-modules'),
    path('create/<int:pk>', views.ModuleGetCreate.as_view(), name='create-module'),
    path('create/', views.ModuleCreate.as_view(), name='create'),
    path('list/', views.ModuleListView.as_view(), name='list'),
]
