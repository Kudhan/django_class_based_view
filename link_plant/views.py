from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Link

class LinkListView(ListView):
    model = Link
    template_name = "link_plant/link_list.html"  # explicitly set template

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    template_name = "link_plant/link_form.html"  # reuse same form
    success_url = reverse_lazy('link-list')       # redirects to list after create

class UpdateLinkView(UpdateView):
    model = Link
    fields = ['text', 'url']                      # only editable fields
    template_name = "link_plant/link_form.html"  # reuse same form
    success_url = reverse_lazy('link-list')       # redirects to list after update
