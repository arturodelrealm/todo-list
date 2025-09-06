from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from services import HuggingFaceEstimate
from tasks.models import Task


class TaskViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tester", password="12345")
        self.client.login(username="tester", password="12345")

        self.task = Task.objects.create(
            title="Test task",
            description="Test description",
            user=self.user,
        )

    def test_task_list_view(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test task")

    @patch.object(HuggingFaceEstimate, 'estimate')
    def test_task_create_view(self, mock_time_estimate):

        mock_time_estimate.return_value = '1 d'

        task_title = 'New Task'
        task_description = 'A task that will take 1 day'
        response = self.client.post(reverse("task_create"), {
            "title": task_title,
            "description": task_description,
        })

        mock_time_estimate.assert_called_once()

        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(title=task_title)
        self.assertEqual(task.description, task_description)
        self.assertEqual(task.time_estimate, '1 d')

    def test_task_update_view(self):
        response = self.client.post(
            reverse("task_update", args=[self.task.pk]), {
                "title": "Edited task",
                "description": "Changed task",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Edited task")

    def test_task_delete_view(self):
        response = self.client.post(
            reverse("task_delete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_complete_and_decomplete(self):
        response = self.client.post(
            reverse("task_complete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

        response = self.client.post(reverse(
            "task_decomplete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertFalse(self.task.completed)

    def test_login_required_redirects(self):
        self.client.logout()
        response = self.client.get(reverse("task_list"))
        self.assertRedirects(
            response, f"/accounts/login/?next={reverse('task_list')}")
