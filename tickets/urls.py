from django.urls import path

from .views import TicketAnalyticsView, TicketDetailView, TicketListCreateView


urlpatterns = [
    path("", TicketListCreateView.as_view(), name="ticket-list-create"),
    path("analytics/", TicketAnalyticsView.as_view(), name="ticket-analytics"),
    path("<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
]