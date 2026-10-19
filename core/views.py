from django.shortcuts import render

def student_dashboard(request):
    context = {
        'wiadomosc' : 'Witaj w panelu studenta!',
    }
    return render(request, 'student_dashboard.html', context)

def lecturer_dashboard(request):
    context = {
        'wiadmosc' : 'Witaj w panelu wykladowcy!',
    }
    return render(request, 'lecturer_dashboard.html', context)
