from django.urls import path
from .views import LinkListView, LinkCreateView, UpdateLinkView

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('create/', LinkCreateView.as_view(), name='create-list'),
    path('<int:pk>/update/', UpdateLinkView.as_view(), name='update-list'),
]
