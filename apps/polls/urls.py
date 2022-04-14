from django.urls import path

from apps.polls.apiviews import PollDetail, PollList

urlpatterns = [
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
]
