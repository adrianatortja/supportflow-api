from django.urls import path

from .views import (
    TicketAnalyticsView,
    TicketCommentListCreateView,
    TicketDetailView,
    TicketListCreateView,
    TicketSuggestedReplyView,
)


urlpatterns = [
    path("", TicketListCreateView.as_view(), name="ticket-list-create"),
    path("analytics/", TicketAnalyticsView.as_view(), name="ticket-analytics"),
    path(
        "<int:pk>/suggested-reply/",
        TicketSuggestedReplyView.as_view(),
        name="ticket-suggested-reply",
    ),
    path(
        "<int:pk>/comments/",
        TicketCommentListCreateView.as_view(),
        name="ticket-comment-list-create",
    ),
    path("<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
]