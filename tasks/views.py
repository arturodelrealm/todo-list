from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .services import TaskVisibilityService


@login_required
def task_list(request):
    task_service = TaskVisibilityService(request.user)
    tasks = task_service.get_queryset().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Tarea creada con éxito!')
            return redirect('task_list')
        messages.error(request, 'Error al crear la tarea.')

    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update(request, pk):
    task_service = TaskVisibilityService(request.user)
    task = task_service.get_object_or_404(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, pk):
    task_service = TaskVisibilityService(request.user)
    task = task_service.get_object_or_404(pk=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, 'Tarea eliminada con éxito.')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_complete(request, pk):
    task_service = TaskVisibilityService(request.user)
    task = task_service.get_object_or_404(pk=pk)
    if not task.completed:
        task.complete()
        messages.success(
            request, f'Tarea "{task.title}" marcada como completada.'
        )
    return redirect('task_list')

@login_required
def task_decomplete(request, pk):
    task_service = TaskVisibilityService(request.user)
    task = task_service.get_object_or_404(pk=pk)
    if task.completed:
        task.decomplete()
        messages.success(
            request, f'Tarea "{task.title}" desmarcada como completada.'
        )
    return redirect('task_list')
