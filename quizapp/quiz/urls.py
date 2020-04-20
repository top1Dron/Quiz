from django.urls import path
from . import views


app_name = 'quiz'


urlpatterns = [
    path('get-module/<int:pk>', views.getModuleAndRedirect, name='get-module'),
    path('create/', views.ChoiceCreate.as_view(), name='create'),
]
