from django.test import TransactionTestCase
from django.db.utils import IntegrityError
from pages.models.page import PageModel


class PageModelTest(TransactionTestCase):
    """Test suite for Page Model"""

    def setUp(self) -> None:
        """"""
        self.page = PageModel(name="YouTube", url="https://youtube.com")
        self.page.save()

    def test_create_page(self):
        self.assertEqual(self.page.name, "YouTube", "Page name doesn't match")
        self.assertEqual(self.page.url, "https://youtube.com",
                         "Page url doesn't match")
        self.assertEqual(self.page.status, "Processing",
                         "Page status doesn't match")
        self.assertEqual(self.page.num_links, 0,
                         "Page num_links doesn't match")

    def test_unique_url(self):
        page2 = PageModel(name="YouTube", url="https://youtube.com")
        with self.assertRaises(IntegrityError):
            page2.save()

    def tearDown(self) -> None:
        self.page.delete()
