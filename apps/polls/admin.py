from django.contrib import admin

from apps.polls.models import Choice, Poll

admin.site.register(Poll)
admin.site.register(Choice)
