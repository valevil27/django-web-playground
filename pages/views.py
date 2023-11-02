from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Page


# Create your views here.
class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    paginate_by = 5


class PageDetailView(DetailView):
    model = Page


class PageCreate(CreateView):
    model = Page
    fields = ["title", "content", "order"]
    success_url = reverse_lazy('pages:pages')
