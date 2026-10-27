from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RegisterForm
from .models import generate_id, User
from django.views.decorators.http import require_POST

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = generate_id()
            user.is_candidate = True
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
    candidates = User.objects.filter(is_student=False, is_lecturer=False, is_candidate=True)
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


@login_required
@require_POST
def accept_student(request, user_id):
    candidate = get_object_or_404(User, id=user_id)
    candidate.is_student = True
    candidate.save()
    return redirect('lecturer_dashboard')


@login_required
@require_POST
def refuse_student(request, user_id):
    candidate = get_object_or_404(User, id = user_id)
    candidate.delete()
    return redirect('lecturer_dashboard')


@login_required
@require_POST
def accept_lecturer(request, user_id):
    candidate = get_object_or_404(User, id=user_id)
    candidate.is_lecturer = True
    candidate.save()
    return redirect('lecturer_dashboard')