from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pages.forms import PageForm
from .models import Page
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    paginate_by = 5


class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, "dispatch")
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, "dispatch")
class PageUpdateView(UpdateView):
    model = Page
    fields = ["title", "content", "order"]
    template_name_suffix = "_update_form"
    def get_success_url(self) -> str:
        return reverse_lazy('pages:update', args=[self.object.id]) + "?ok" # type: ignore

@method_decorator(staff_member_required, "dispatch")
class PageDeleteView(DeleteView):
    model = Page
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy('pages:pages')
