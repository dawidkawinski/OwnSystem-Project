from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('wykladowca/przeglad', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('przeglad/', views.lecturer_master, name='lecturer_master'),
    path('przedmioty/', views.lecturer_courses, name='lecturer_courses'),
    path('wnioski/', views.lecturer_requests, name='lecturer_requests'),
    path('wiadomosci/', views.lecturer_messages, name='lecturer_messages'),
    path('studenci/przeglad-student', views.lecturer_students, name='lecturer_students'),
    path('przeglad-student/', views.student_master, name='student_master'),
    path('przedmioty-student/', views.student_courses, name='student_courses'),
    path('oceny/', views.student_grades, name='student_grades'),
    path('wiadomosci-student/', views.student_messages, name='student_messages'),
    path('start/', views.role_redirect, name='role_redirect'),
    path('rejestracja/', views.register, name='register'),
    path('rejestracja/sukces', views.register_success, name='register_success'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('przyjmij/<int:user_id>/', views.accept_student, name='accept_student'),
    path('odrzuc/<int:user_id>/', views.refuse_student, name='refuse_student'),
    path('wykladowca/<int:user_id>/', views.accept_lecturer, name='accept_lecturer'),
    path('oceny/usun/<int:grade_id>/', views.delete_grade, name='delete_grade'),
]
