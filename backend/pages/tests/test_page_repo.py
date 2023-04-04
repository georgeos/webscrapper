from django.test import TestCase
from django.db.utils import IntegrityError
from pages.models.page import PageModel
from pages.repositories.page_repo import PageRepo


class PageRepoTest(TestCase):
    """Test suite for Page Model"""

    def setUp(self) -> None:
        """"""
        page1 = PageModel(name="YouTube", url="https://youtube.com")
        page2 = PageModel(name="Google", url="https://google.com")
        page3 = PageModel(name="Microsoft", url="https://microsoft.com")
        pages = [page1, page2, page3]
        PageModel.objects.bulk_create(pages)

    def test_get_page(self):
        page = PageRepo.get(id=1)
        self.assertEqual(page.name, "YouTube", "Name doesn't match")
        self.assertEqual(page.url, "https://youtube.com", "Url doesn't match")

    def test_create_page(self):
        page, created = PageRepo.update_create(
            {"name": "Yahoo"}, url="https://yahoo.com")
        self.assertEqual(page.name, "Yahoo", "Name doesn't match")
        self.assertEqual(page.url, "https://yahoo.com", "Url doesn't match")
        self.assertEqual(created, True, "Page was created")

    def test_update_page(self):
        page, created = PageRepo.update_create(
            {"name": "Yahoo"}, url="https://google.com")
        self.assertEqual(page.name, "Yahoo", "Name doesn't match")
        self.assertEqual(page.url, "https://google.com", "Url doesn't match")
        self.assertEqual(created, False, "Page wasn't created")

    def test_all_pages(self):
        pages = PageRepo.all()
        self.assertEqual(pages.count(), 3, "Number of objects doesn't match")

    def tearDown(self) -> None:
        PageModel.objects.all().delete()
