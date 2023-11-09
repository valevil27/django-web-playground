from django.urls import path

from messenger.views import ThreadDetailView, ThreadView


messenger_patterns = ([
    
    path("", ThreadView.as_view(), name="list"),
    path("thread/<int:pk>", ThreadDetailView.as_view(), name="detail"),
    ],"messenger")