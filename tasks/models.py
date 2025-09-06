from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):

    DAY_TO_DUES_SOON = 2

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True)

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    time_estimate = models.TextField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def complete(self):
        self.completed = True
        self.completed_at = timezone.now()
        self.save()

    def decomplete(self):
        self.completed = False
        self.completed_at = None
        self.save()

    def is_overdue(self):
        if self.completed:
            return False
        today = timezone.now().date()
        return self.due_date and self.due_date < today

    def is_due_soon(self):
        if self.completed:
            return False
        today = timezone.now().date()
        return self.due_date and \
           today <= self.due_date <= \
           today + timedelta(days=self.DAY_TO_DUES_SOON)
