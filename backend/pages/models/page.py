from django.db import models


class PageModel(models.Model):
    """Model to manage pages searched by end user"""
    name = models.CharField(max_length=75)
    url = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=25, default="Processing")
    num_links = models.IntegerField(default=0)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"Page {self.name} ({self.url}) has {self.num_links} link(s)"
