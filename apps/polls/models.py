from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Poll(models.Model):
    question = models.CharField(_("Question"), max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Created by"))
    pub_date = models.DateTimeField(_("Publication date"), auto_now=True)

    def __str__(self) -> str:
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name=_("Poll"), related_name="choices")
    choice_text = models.CharField(_("Choice Text"), max_length=100)

    def __str__(self) -> str:
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name=_("Choice"), related_name="votes")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name=_("Poll"), related_name="votes")
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Voted by"))

    class Meta:
        unique_together = ("poll", "voted_by")
