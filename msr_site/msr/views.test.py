from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from msr.models import Task_board
from msr.forms import AddProjectForm

class AddProjectViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.add_project_url = reverse('add_project')

