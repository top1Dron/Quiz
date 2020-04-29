from django.urls import path
from . import views


app_name = 'modules'


urlpatterns = [
    path('get-subject-modules/<int:pk>', views.ModuleListView.as_view(), name='get-subject-modules'),
    path('get-subject/<int:pk>', views.getSubjectAndRedirect, name='get-subject'),
    path('create/', views.ModuleCreate.as_view(), name='create'),
    path('update/<int:pk>', views.ModuleUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.ModuleDelete.as_view(), name='delete'),
    # path('list/', views.ModuleListView.as_view(), name='list'),
]
