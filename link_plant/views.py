from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .models import Link,Profile

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

class DeleteLinkView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')       # redirects to list after delete
    template_name = "link_plant/link_confirm_delete.html"  # confirm delete template

def profile_view(request,profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links=profile.links.all()
    context={
        'profile':profile,
        'links':links
    }

    return render(request,'link_plant/profile.html',context)