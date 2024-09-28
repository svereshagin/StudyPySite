from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import subprocess

def home(request):
    return render(request, 'home.html', )

def lecture(request):
    return render(request, 'lecture.html', )

def tasks(request):
    result = None
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            # Внимание: выполнение пользовательского кода через subprocess небезопасно.
            # Это только для примера.
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True, text=True, check=True
            ).stdout
        except subprocess.CalledProcessError as e:
            result = e.stderr

    # Передаем result в шаблон
    return render(request, 'tasks.html', {'result': result})

