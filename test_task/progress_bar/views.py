from django.shortcuts import render
from .tasks import long_running_task
from django.http import JsonResponse, HttpResponse, HttpRequest
import uuid

def index(request: HttpRequest) -> HttpResponse:
    """
    La vista para la página principal
    """
    return render(request, 'progress_bar/index.html')

def start_task(request: HttpRequest) -> JsonResponse:
    """
    La vista que acepta solo POST, para iniciar una nueva tarea.
    Primero se genera task_id, y luego este es usado para la tarea de Celery long_running_task.
    Después devuelve JsonResponse con el estatus y task_id
    """
    if request.method == 'POST':
        task_id = str(uuid.uuid4())
        long_running_task.apply_async(kwargs={'task_id': task_id})
        return JsonResponse({"status": "Task started successfully", "task_id": task_id})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)