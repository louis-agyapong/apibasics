from django.urls import include, path

from apps.polls.apiviews import (
    ChoiceList,
    CreateVote,
    LoginView,
    PollDetail,
    PollList,
    UserCreate,
)

urlpatterns = [
    path(
        "polls/",
        include(
            [
                path("", PollList.as_view(), name="polls_list"),
                path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
                path("<int:pk>/choices/", ChoiceList.as_view(), name="choices_list"),
                path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
            ]
        ),
    ),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
