import requests
from typing import List
from bs4 import BeautifulSoup
from pages.exceptions import ScrapperException
from pages.models.link import LinkModel


class Scrapper():
    """Class to scap web pages"""

    @staticmethod
    def scrape_page(page_url: str) -> BeautifulSoup:
        """Scrap a web page"""
        response = requests.get(page_url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            raise ScrapperException()

    def scrape_page_tile(self, page_url: str) -> str:
        """Scrap page title"""
        soup = self.scrape_page(page_url)
        return soup.title.string

    def scrape_all_href(self, page_url: str) -> List[LinkModel]:
        """Scrap all href elements in a web page"""
        soup = self.scrape_page(page_url)
        links = []

        for a in soup.find_all("a"):
            name = a.text
            url = a.get("href")
            if url:
                link = LinkModel(name=name, url=url)
                links.append(link)
        return links
