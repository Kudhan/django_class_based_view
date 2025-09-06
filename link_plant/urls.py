from django.urls import path
from .views import LinkListView, LinkCreateView, UpdateLinkView,DeleteLinkView,profile_view

urlpatterns = [
    path('manage/', LinkListView.as_view(), name='link-list'),
    path('create/', LinkCreateView.as_view(), name='create-list'),
    path('<int:pk>/update/', UpdateLinkView.as_view(), name='update-list'),
    path('<int:pk>/delete/', DeleteLinkView.as_view(), name='delete-list'),
    path('<slug:profile_slug>', profile_view, name='profile'),
]
