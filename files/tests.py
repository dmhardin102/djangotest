from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Document


class AuthTests(TestCase):
    def test_signup_creates_user(self):
        response = self.client.post(reverse("files:signup"), {
            "username": "newuser",
            "password1": "ComplexPwd123",
            "password2": "ComplexPwd123",
        })
        self.assertRedirects(response, reverse("files:login"))
        self.assertEqual(User.objects.filter(username="newuser").count(), 1)

    def test_document_list_requires_login(self):
        response = self.client.get(reverse("files:document_list"))
        self.assertRedirects(response, "/files/login/?next=/files/")


class UploadTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_user(username="staff", password="pass", is_staff=True)
        self.user = User.objects.create_user(username="user", password="pass")

    def test_staff_can_upload(self):
        self.client.login(username="staff", password="pass")
        upload = SimpleUploadedFile("test.txt", b"filecontent")
        response = self.client.post(reverse("files:upload_document"), {"title": "Test", "file": upload})
        self.assertRedirects(response, reverse("files:document_list"))
        self.assertEqual(Document.objects.count(), 1)

    def test_non_staff_cannot_upload(self):
        self.client.login(username="user", password="pass")
        upload = SimpleUploadedFile("test.txt", b"filecontent")
        response = self.client.post(reverse("files:upload_document"), {"title": "Test", "file": upload})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Document.objects.count(), 0)
