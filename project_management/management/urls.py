from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, UserProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]
