from django.db import models
from pages.models.page import PageModel
from pages.fields import TruncatedCharField


class LinkModel(models.Model):
    """Model to manage links related to a page searched by end user"""
    name = TruncatedCharField(max_length=75)
    url = models.CharField(max_length=255)
    page = models.ForeignKey(PageModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"Link {self.name} ({self.url})"
