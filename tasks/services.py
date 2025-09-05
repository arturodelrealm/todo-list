from django.shortcuts import get_object_or_404

from .models import Task


class BaseService:

    def __init__(self, user):
        self.user = user

    @staticmethod
    def get_queryset():
        raise NotImplementedError

    def can_view(self, task):
        return self.get_queryset().filter(pk=task.pk).exists()

    def get_object_or_404(self, **kwargs):
        return get_object_or_404(self.get_queryset(), **kwargs)

    def can_edit(self, task) -> bool:
        return self.can_view(task)

    def can_delete(self, task) -> bool:
        return self.can_view(task)


class TaskVisibilityService(BaseService):

    @staticmethod
    def get_queryset():
        return Task.objects.all()
