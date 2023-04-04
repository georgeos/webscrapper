import logging
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from pages.exceptions import ScrapperException
from pages.scrapper import Scrapper
from pages.models.link import LinkModel
from pages.repositories.link_repo import LinkRepo
from pages.repositories.page_repo import PageRepo


@shared_task
def parse_links(page_id: int):
    """Task to process links for an specific page_id.

    It deletes and creates links (updates the list) for the page, in case the page already exists.
    """
    try:
        page = PageRepo.get(id=page_id)
        scrapper = Scrapper()
        links = scrapper.scrape_all_href(page.url)
        links = [LinkModel(name=l.name, url=l.url, page=page) for l in links]

        LinkRepo.filter_delete(page_id=page_id)
        LinkRepo.bulk_create(links)

        num_links = len(links)
        PageRepo.update_create(id=page_id, defaults={
                               "status": "Processed", "num_links": num_links})

    except ObjectDoesNotExist:
        logging.error(f"Page not found {page.url}")
    except ScrapperException:
        logging.error(f"Error while scrapping page {page.url}")
