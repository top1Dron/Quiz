from django.urls import path
from . import views


app_name = 'subjects'


urlpatterns = [
    path('create/', views.SubjectCreate.as_view(), name='create'),
    path('list/', views.SubjectListView.as_view(), name='list'),
    path('update/<int:pk>', views.SubjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.SubjectDelete.as_view(), name='delete'),
]