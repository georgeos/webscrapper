from django.test import TestCase
from pages.models.link import LinkModel
from pages.models.page import PageModel


class PageModelTest(TestCase):
    """Test suite for Page Model"""

    def test_url_length(self):
        page = PageModel(name="Youtube", url="https://youtube.com")
        page.save()

        link = LinkModel.objects.create(
            name="""<div id='mypagediv2' style='position:relative;text-align:center;'><h2>Related Pages</h2></div>""",
            url="https://youtube.com/1",
            page=page)
        link = LinkModel.objects.get(url="https://youtube.com/1")
        lenght = len(link.name)
        self.assertEqual(lenght, 75, "Url lenght should be 75 chars max")
        self.assertEqual(
            link.name, "<div id='mypagediv2' style='position:relative;text-align:center;'><h2>Relat", "Name doesn't match")
