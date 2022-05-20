from django.contrib import admin

from apps.polls.models import Choice, Poll, Vote


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("question", "created_by", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["question"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("poll", "choice_text")
    search_fields = ["choice_text"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("poll", "choice", "voted_by")
    search_fields = ["poll", "choice", "voted_by"]
