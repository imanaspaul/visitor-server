from django.urls import path
from . views import AllEntry, update_log_entry

# Entry urls
urlpatterns = [
    path("all-entry/", AllEntry.as_view()),
    path("update-entry/", update_log_entry),
]
