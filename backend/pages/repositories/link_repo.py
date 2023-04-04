from typing import List
from pages.models.link import LinkModel


class LinkRepo():
    """Class to manage communication with LinkModel."""

    @classmethod
    def all(self) -> List[LinkModel]:
        """Returns all existing LinkModel."""
        return LinkModel.objects.all()

    @classmethod
    def filter(self, **kwargs) -> List[LinkModel]:
        """Returns a List of LinkModel."""
        return LinkModel.objects.filter(**kwargs)

    @classmethod
    def filter_delete(self, **kwargs) -> None:
        """Filters and deletes a LinkModel based on args."""
        LinkModel.objects.filter(**kwargs).delete()

    @classmethod
    def bulk_create(self, models: List[LinkModel]) -> None:
        """Bulk insert a list of LinkModel."""
        return LinkModel.objects.bulk_create(models)
