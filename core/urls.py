from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('wykladowca/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('start/', views.role_redirect, name='role_redirect'),
    path('rejestracja/', views.register, name='register'),
    path('rejestracja/sukces', views.register_success, name='register_success'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('przyjmij/<int:user_id>/', views.accept_student, name='accept_student'),
    path('odrzuc/<int:user_id>/', views.refuse_student, name='refuse_student'),
    path('wykladowca/<int:user_id>/', views.accept_lecturer, name='accept_lecturer'),
]
