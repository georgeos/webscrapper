from rest_framework import serializers
from pages.models.link import LinkModel


class LinkSerializer(serializers.ModelSerializer):
    """Serializer for Page model"""
    class Meta:
        model = LinkModel
        fields = ["id", "name", "url"]
