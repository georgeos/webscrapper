from django.test import TestCase
from pages.models.page import PageModel
from pages.models.link import LinkModel
from pages.repositories.page_repo import PageRepo
from pages.repositories.link_repo import LinkRepo


class LinkRepoTest(TestCase):
    """Test suite for Page Model"""

    def setUp(self) -> None:
        """"""
        url = "https://youtube.com"
        self.page = PageModel(name="YouTube", url=url)
        self.page.save()

        link1 = LinkModel(name="Link1", url=f"{url}/1", page=self.page)
        link2 = LinkModel(name="Link2", url=f"{url}/2", page=self.page)
        link3 = LinkModel(name="Link3", url=f"{url}/3", page=self.page)
        link4 = LinkModel(name="Link4", url=f"{url}/4", page=self.page)
        link5 = LinkModel(name="Link5", url=f"{url}/5", page=self.page)
        self.links = [link1, link2, link3, link4, link5]

    def test_bulk_create(self):
        LinkRepo.bulk_create(self.links)
        links = LinkRepo.all()
        self.assertEqual(links.count(), 5, "Number of links doesn't match")
        self.assertEqual(links[0].name, "Link1", "Link name doesn't match")
        self.assertEqual(
            links[0].url, "https://youtube.com/1", "Link name doesn't match")

    def test_filter(self):
        LinkRepo.bulk_create(self.links)
        links = LinkRepo.filter(name="Link5")
        self.assertEqual(links.count(), 1, "Number of links doesn't match")
        self.assertEqual(
            links[0].url, "https://youtube.com/5", "Link name doesn't match")

    def test_filter_delete(self):
        LinkRepo.bulk_create(self.links)
        LinkRepo.filter_delete(name="Link5")
        links = LinkRepo.all()
        self.assertEqual(links.count(), 4, "Number of links doesn't match")

    def tearDown(self) -> None:
        self.page.delete()
