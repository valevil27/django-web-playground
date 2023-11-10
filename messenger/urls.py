from django.urls import path

from messenger.views import ThreadDetailView, ThreadView, add_message


messenger_patterns = ([
    path("", ThreadView.as_view(), name="list"),
    path("thread/<int:pk>/", ThreadDetailView.as_view(), name="detail"),
    path("thread/<int:pk>/add/", add_message, name="add"),
    ],"messenger")