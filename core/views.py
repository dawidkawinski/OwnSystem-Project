from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required
def student_dashboard(request):
    if not request.user.is_student:
            raise PermissionDenied
    context = {
        'wiadomosc' : 'Witaj w panelu studenta!',
    }
    return render(request, 'student_dashboard.html', context)

@login_required
def lecturer_dashboard(request):
    if not request.user.is_lecturer:
        raise PermissionDenied
    context = {
        'wiadomosc' : 'Witaj w panelu wykladowcy!',
    }
    return render(request, 'lecturer_dashboard.html', context)

@login_required
def role_redirect(request):
    if request.user.is_lecturer:
        return redirect('lecturer_dashboard')
    elif request.user.is_student:
        return redirect('student_dashboard')
    else:
        return redirect('/admin/')

@login_required
def przycisk(request):
    if request.method == 'POST':
        print('Kliknieto przycisk')
    return redirect('role_redirect')