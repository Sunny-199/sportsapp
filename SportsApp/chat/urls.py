from django.urls import path, re_path
#
#
from .views import ThreadView, InboxView

urlpatterns = [
    path("", InboxView.as_view()),
    re_path(r"^(?P<chat_room>[\w.@+-]+)/$", ThreadView.as_view()),
]
