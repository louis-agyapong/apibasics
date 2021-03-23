from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    name = models.CharField(_("name"), max_length=100)
    score = models.DecimalField(_("score"), max_digits=6, decimal_places=3)

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return self.name
