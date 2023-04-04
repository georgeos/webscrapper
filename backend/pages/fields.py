from django.db import models


class TruncatedCharField(models.CharField):
    """Field to truncate the value to the max_lenght"""

    def get_prep_value(self, value):
        value = super(TruncatedCharField, self).get_prep_value(value)
        if value:
            return value[:self.max_length]
        return value
