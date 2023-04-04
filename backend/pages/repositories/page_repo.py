from typing import List, Tuple
from pages.models.page import PageModel


class PageRepo():
    """Class to manage communication with PageModel."""

    @classmethod
    def get(self, id: int) -> PageModel:
        """Returns a PageModel based on id."""
        return PageModel.objects.get(id=id)

    @classmethod
    def all(self) -> List[PageModel]:
        """Returns all existing PageModel."""
        return PageModel.objects.all()

    @classmethod
    def update_create(self, defaults: dict, **kwargs) -> Tuple[PageModel, bool]:
        """Updates or creates based on args."""
        page, created = PageModel.objects.update_or_create(
            defaults=defaults, **kwargs)
        return page, created
