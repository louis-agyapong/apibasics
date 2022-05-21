from django.urls import path, include

from apps.polls.apiviews import PollDetail, PollList, ChoiceList, CreateVote

urlpatterns = [
    path("polls/", include([
        path("", PollList.as_view(), name="polls_list"),
        path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
        path("<int:pk>/choices/", ChoiceList.as_view(), name="choices_list"),
        path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

    ]))
]
