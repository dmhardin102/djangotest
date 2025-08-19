from django.db import models


class Document(models.Model):
    """A file uploaded by an admin for users to download."""

    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return self.title or self.file.name

