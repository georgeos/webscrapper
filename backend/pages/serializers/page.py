from rest_framework import serializers
from pages.models.page import PageModel


class PageSerializer(serializers.ModelSerializer):
    """Serializer for Page model"""
    class Meta:
        model = PageModel
        fields = ["id", "name", "url", "status", "num_links"]
