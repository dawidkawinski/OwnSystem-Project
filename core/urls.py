from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('wykladowca/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('start/', views.role_redirect, name='role_redirect'),
]
