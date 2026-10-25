from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RegisterForm
from .models import generate_id, User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = generate_id()
            # user.is_student = True
            user.save()
            login(request, user)
            request.session['new_id'] = user.username
            return redirect('register_success')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})     


@login_required
def register_success(request):
    id = request.session.pop('new_id', None)
    if not id:
        return redirect('role_redirect')
    return render(request, 'registration/success.html', {'id': id})


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
    candidates = User.objects.filter(is_student=False, is_lecturer=False)
    context = {
        'wiadomosc' : 'Witaj w panelu wykladowcy!',
        'candidates': candidates
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

