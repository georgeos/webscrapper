from django.test import TestCase
from requests.exceptions import ConnectionError
from pages.scrapper import Scrapper
from pages.exceptions import ScrapperException


class ScrapperTest(TestCase):
    """Test suite for the scrapper"""

    def setUp(self) -> None:
        self.scrapper = Scrapper()
        self.url = "https://www.blank.org/"

    def test_connection_error(self):
        with self.assertRaises(ConnectionError):
            self.scrapper.scrape_page("https://doesntexist")

    def test_scrapper_exception(self):
        with self.assertRaises(ScrapperException):
            self.scrapper.scrape_page("https://google.com/login")

    def test_scrape_title_page(self):
        title = self.scrapper.scrape_page_tile(self.url)
        self.assertEqual(title, "\nblank\n", "Title is not matching")

    def test_scrape_links_blank_page(self):
        links = self.scrapper.scrape_all_href(self.url)
        lenght = len(links)
        self.assertEqual(lenght, 1, "Num of links are not matching")

    def test_scrape_link_name_blank_page(self):
        links = self.scrapper.scrape_all_href(self.url)
        self.assertEqual(links[0].name, ".", "Link name not matching")

    def test_scrape_link_href_blank_page(self):
        links = self.scrapper.scrape_all_href(self.url)
        self.assertEqual(links[0].url, "blank.html", "href not matching")
