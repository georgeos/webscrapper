from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from pages.serializers.link import LinkSerializer
from pages.repositories.link_repo import LinkRepo


class LinkView(ModelViewSet):
    """View to handle page related requests"""
    pagination_class = PageNumberPagination

    def list(self, request, page_id: int):
        """Return all pages scrapped"""
        links = LinkRepo.filter(page_id=page_id)
        page = self.paginate_queryset(links)
        serializer = LinkSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
