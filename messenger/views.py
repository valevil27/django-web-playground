from __future__ import annotations
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from messenger.models import Thread, Message

# Create your views here.


@method_decorator(login_required, "dispatch")
class ThreadView(TemplateView):
    template_name = "messenger/thread_list.html"


@method_decorator(login_required, "dispatch")
class ThreadDetailView(DetailView):
    model = Thread
    template_name = "messenger/thread_detail.html"

    def get_object(self, queryset=None):
        obj: Thread = super().get_object(queryset)  # type: ignore
        if self.request.user not in obj.users.all():
            return Http404()
        return obj


def add_message(request: HttpRequest, pk: int):
    json_resp = {"created": False}
    if not request.user.is_authenticated:
        raise Http404("User is not authenticated")
    content = request.GET.get("content", None)
    if not content:
        return JsonResponse(json_resp)
    thread = get_object_or_404(Thread, pk=pk)
    message = Message.objects.create(user=request.user, content=content)
    thread.messages.add(message)
    json_resp["created"] = True
    return JsonResponse(json_resp)
