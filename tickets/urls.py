from django.urls import path

from .views import TicketDetailView, TicketListCreateView


urlpatterns = [
    path('', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]
