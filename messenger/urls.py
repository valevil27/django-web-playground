from django.urls import path

from messenger.views import ThreadDetailView, ThreadView, add_message, start_thread


messenger_patterns = ([
    path("", ThreadView.as_view(), name="list"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="detail"),
    path("thread/start/<username>", start_thread, name="start"),
    path("thread/<int:pk>/add/", add_message, name="add"),
    ],"messenger")