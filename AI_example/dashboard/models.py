# FILE PURPOSE: Placeholder for Django ORM models (not used in this CSV-based tutorial).
# NEXT: open dashboard/admin.py to see how ExampleRecord appears in the Django admin interface.

# IMPORT: models is Django's ORM toolkit for defining database tables as Python classes.
from django.db import models


# CLASS: ExampleRecord is a sample model showing where future database schema would live.
# WHY: Even though this tutorial reads a CSV directly, seeing a model helps beginners spot where ORM code belongs.
class ExampleRecord(models.Model):
    # COMMENT: sample_name demonstrates a text field; blank=True so it can stay optional for this demo.
    sample_name = models.CharField(max_length=100, blank=True)

    # COMMENT: __str__ defines a readable string representation for admin panels and debugging.
    def __str__(self) -> str:
        return self.sample_name or "Unnamed Record"

    class Meta:
        # COMMENT: verbose_name_plural controls how Django labels this model in the admin site.
        verbose_name_plural = "Example Records"
