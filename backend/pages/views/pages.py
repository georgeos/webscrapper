from requests.exceptions import ConnectionError
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from pages.serializers.page import PageSerializer
from pages.scrapper import Scrapper
from pages.exceptions import ScrapperException
from pages.repositories.page_repo import PageRepo
from pages.tasks.parse_links import parse_links


class PageView(ModelViewSet):
    """View to handle page related requests"""
    pagination_class = PageNumberPagination

    def list(self, request):
        """Return all pages scrapped"""
        pages = PageRepo.all()
        page = self.paginate_queryset(pages)
        serializer = PageSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        """Scrap a new page"""
        data = request.data
        scrapper = Scrapper()
        url = data["url"]

        try:
            name = scrapper.scrape_page_tile(url)
            page, _ = PageRepo.update_create(
                defaults={"name": name, "status": "Processing"}, url=url)
            page_serializer = PageSerializer(page)
            parse_links.delay(page.pk)
            return Response(page_serializer.data, status=status.HTTP_200_OK)

        except (ConnectionError, ScrapperException):
            return Response(status=status.HTTP_400_BAD_REQUEST)
