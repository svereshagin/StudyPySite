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
        input_data = request.POST.get('input_data', '')  # Получаем данные для input()

        # Заменяем input() на заданные данные
        if 'input()' in code:
            code = code.replace('input()', f'"{input_data}"')

        try:
            result = subprocess.run(
                ['python3', '-c', code],
                capture_output=True, text=True, check=True
            ).stdout
        except subprocess.CalledProcessError as e:
            result = e.stderr

    return render(request, 'tasks.html', {'result': result})

