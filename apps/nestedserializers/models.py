from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(_("title"), max_length=100)
    ratings = models.IntegerField(_("ratings"))
    author = models.ForeignKey(Author, verbose_name=_("author"), on_delete=models.CASCADE, related_name="books")

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return f"{self.first_name} {self.title}"
