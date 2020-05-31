from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Item(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'A', _('Active')
        DONE = 'D', _('Done')


    description = models.CharField(max_length=200)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
