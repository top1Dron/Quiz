from django.urls import path
from . import views


app_name = 'quiz'


urlpatterns = [
    path('get-module/<int:pk>', views.getModuleAndRedirect, name='get-module'),
    path('get-module-questions/<int:pk>', views.QuestionList.as_view(), name='get-module-questions'),
    path('create/', views.ChoiceCreate.as_view(), name='create'),
]
