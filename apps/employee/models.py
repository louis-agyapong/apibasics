from django.db import models
from django.utils.translation import ugettext_lazy as _


class Employee(models.Model):
    name = models.CharField(_("name"), max_length=50)
    salary = models.DecimalField(_("salary"), max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name
