from django.shortcuts import render
from .tasks import long_running_task
from django.http import JsonResponse


def index(request):
    return render(request, 'progress_bar/index.html')


def start_task(request):
    if request.method == 'POST':
        long_running_task.delay()
        return JsonResponse({"status": "Task started successfully"})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
