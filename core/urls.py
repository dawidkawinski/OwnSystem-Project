from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_dashboard, name='student_panel'),
    path('wykladowca/', views.lecturer_dashboard, name='lecturer_panel'),
]
