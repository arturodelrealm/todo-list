from datetime import datetime, timezone as dt_timezone
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task


class TaskViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester", password="12345")

        self.task = Task.objects.create(
            title="Test task",
            description="Test description",
            user=self.user,
        )

    @patch('django.utils.timezone.now')
    def test_task_is_overdue(self, timezone_mock):
        timezone_mock.return_value = datetime(
            2025, 1, 1, 12, 0, 0,
            tzinfo=dt_timezone.utc
        )
        self.assertFalse(self.task.is_overdue())

        self.task.due_date = datetime(
            2026, 1, 1,
            tzinfo=dt_timezone.utc
        ).date()
        self.assertFalse(self.task.is_overdue())

        self.task.due_date = datetime(
            2024, 1, 1,
            tzinfo=dt_timezone.utc
        ).date()
        self.assertTrue(self.task.is_overdue())

        self.task.complete()
        self.assertFalse(self.task.is_overdue())

    @patch('django.utils.timezone.now')
    def test_task_is_due_soon(self, timezone_mock):
        timezone_mock.return_value = datetime(
            2025, 1, 1, 12, 0, 0,
            tzinfo=dt_timezone.utc
        )
        self.assertFalse(self.task.is_due_soon())

        self.task.due_date = datetime(
            2026, 1, 1,
            tzinfo=dt_timezone.utc
        ).date()
        self.assertFalse(self.task.is_due_soon())

        self.task.due_date = datetime(
            2024, 1, 1,
            tzinfo=dt_timezone.utc
        ).date()
        self.assertFalse(self.task.is_due_soon())

        self.task.due_date = datetime(
            2025, 1, 2,
            tzinfo=dt_timezone.utc
        ).date()
        self.assertTrue(self.task.is_due_soon())

        self.task.complete()
        self.assertFalse(self.task.is_due_soon())
