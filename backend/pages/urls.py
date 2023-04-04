from django.urls import include, path
from rest_framework.routers import DefaultRouter
from pages.views.pages import PageView
from pages.views.links import LinkView

router = DefaultRouter()
router.register('pages', PageView, basename="pages")
router.register(r'pages/(?P<page_id>[\w-]+)/links', LinkView, basename="links")

urlpatterns = [
    path('', include(router.urls))
]
