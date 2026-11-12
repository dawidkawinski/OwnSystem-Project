from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RegisterForm
from .models import generate_id, User, Ocena
from django.views.decorators.http import require_POST
from django.db.models import Avg

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

#STUDENT SITE
@login_required
def student_dashboard(request):
    if not request.user.is_student:
        raise PermissionDenied
    return render(request, 'student_dashboard.html')

@login_required
def student_master(request):
    if not request.user.is_student:
        raise PermissionDenied
    oceny = Ocena.objects.filter(student=request.user).order_by('-data_wystawienia', '-id')
    srednia = oceny.aggregate(Avg('wartosc'))['wartosc__avg']
    context = {
        'grades_count': oceny.count(),
        'average_grade': round(srednia, 2) if srednia else '-',
        'recent_grades': oceny[:5],
    }
    return render(request, 'student_master.html', context)

@login_required
def student_courses(request):
    if not request.user.is_student:
        raise PermissionDenied
    przedmioty = Ocena.objects.filter(student=request.user).values_list('przedmiot', flat=True).distinct()
    return render(request, 'student_courses.html', {'przedmioty': przedmioty})

@login_required
def student_grades(request):
    if not request.user.is_student:
        raise PermissionDenied
    oceny = Ocena.objects.filter(student=request.user).order_by('-data_wystawienia', '-id')
    return render(request, 'student_grades.html', {'oceny': oceny})

@login_required
def student_messages(request):
    if not request.user.is_student:
        raise PermissionDenied
    return render(request, 'student_messages.html')
#END OF STUDENT SITE

#LECTURER SITE
@login_required
def lecturer_dashboard(request):
    if not request.user.is_lecturer:
        raise PermissionDenied
    return render(request, 'lecturer_dashboard.html')

@login_required
def lecturer_master(request):
    if not request.user.is_lecturer:
            raise PermissionDenied
    pending = User.objects.filter(is_candidate=True, is_student=False, is_lecturer=False)
    context = {
        'pending_count': pending.count(),
        'students_count': User.objects.filter(is_student=True).count(),
        'lecturers_count': User.objects.filter(is_lecturer=True).count(),
        'recent_requests': pending.order_by('-date_joined')[:5],
    }
    return render(request, 'lecturer_master.html', context)

@login_required
def lecturer_courses(request):
    if not request.user.is_lecturer:
        raise PermissionDenied
    if request.method == 'POST':
        student_username = request.POST.get('student')
        przedmiot = request.POST.get('przedmiot')
        wartosc = request.POST.get('wartosc')
        
        if student_username and przedmiot and wartosc:
            student_obj = get_object_or_404(User, username=student_username, is_student=True)
            Ocena.objects.create(
                student=student_obj,
                przedmiot=przedmiot,
                wartosc=wartosc
            )
            return redirect('lecturer_courses')

    students = User.objects.filter(is_student=True).order_by('last_name', 'first_name')
    oceny = Ocena.objects.select_related('student').order_by('-data_wystawienia', '-id')
    context = {
        'students': students,
        'oceny': oceny,
    }
    return render(request, 'lecturer_courses.html', context)

@login_required
@require_POST
def delete_grade(request, grade_id):
    if not request.user.is_lecturer:
        raise PermissionDenied
    ocena = get_object_or_404(Ocena, id=grade_id)
    ocena.delete()
    return redirect('lecturer_courses')

@login_required
def lecturer_requests(request):
    if not request.user.is_lecturer:
            raise PermissionDenied
    candidates = User.objects.filter(is_student=False, is_lecturer=False, is_candidate=True)
    context = {
            'candidates': candidates
        }
    return render(request, 'lecturer_requests.html', context)

@login_required
def lecturer_students(request):
    if not request.user.is_lecturer:
                raise PermissionDenied
    students = User.objects.filter(is_student=True).order_by('last_name', 'first_name')
    context = {
         'students': students
    }
    return render(request, 'lecturer_students.html', context)

@login_required
def lecturer_messages(request):
    if not request.user.is_lecturer:
                raise PermissionDenied
    return render(request, 'lecturer_messages.html')
#END OF LECTURER SITE

@login_required
def role_redirect(request):
    if request.user.is_lecturer:
        return redirect('lecturer_master')
    elif request.user.is_student:
        return redirect('student_master')
    else:
        return redirect('/admin/')


@login_required
@require_POST
def accept_student(request, user_id):
    candidate = get_object_or_404(User, id=user_id)
    candidate.is_student = True
    candidate.save()
    return redirect('lecturer_requests')


@login_required
@require_POST
def refuse_student(request, user_id):
    candidate = get_object_or_404(User, id = user_id)
    candidate.delete()
    return redirect('lecturer_requests')


@login_required
@require_POST
def accept_lecturer(request, user_id):
    candidate = get_object_or_404(User, id=user_id)
    candidate.is_lecturer = True
    candidate.save()
    return redirect('lecturer_requests')