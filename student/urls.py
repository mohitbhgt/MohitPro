
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('create/', views.create_student, name='create'),
    path('edit/<uuid:pk>', views.edit_student, name='edit'),
    path('delete/<uuid:pk>', views.delete_student, name='delete'),
]