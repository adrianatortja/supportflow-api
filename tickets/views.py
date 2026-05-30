from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ticket, TicketComment
from .serializers import TicketCommentSerializer, TicketSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "priority",
        "organization",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
        "priority",
        "status",
    ]

    ordering = ["-created_at"]

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


class TicketAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tickets = Ticket.objects.filter(owner=request.user)

        total_tickets = tickets.count()

        status_counts = tickets.values("status").annotate(count=Count("id"))
        priority_counts = tickets.values("priority").annotate(count=Count("id"))

        data = {
            "total_tickets": total_tickets,
            "status_counts": {
                item["status"]: item["count"] for item in status_counts
            },
            "priority_counts": {
                item["priority"]: item["count"] for item in priority_counts
            },
        }

        return Response(data)


class TicketSuggestedReplyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        ticket = get_object_or_404(
            Ticket,
            pk=pk,
            owner=request.user,
        )

        suggested_reply = (
            "Hi, thank you for reaching out. "
            "I’m sorry you’re experiencing this issue. "
            "We’ll review your request and get back to you as soon as possible."
        )

        title = ticket.title.lower()
        description = ticket.description.lower()

        if (
            "login" in title
            or "login" in description
            or "access" in title
            or "access" in description
            or "password" in title
            or "password" in description
        ):
            suggested_reply = (
                "Hi, thank you for reaching out. "
                "I’m sorry you’re having trouble accessing your account. "
                "Please try resetting your password again, and if the issue continues, "
                "we’ll investigate further."
            )

        elif "refund" in title or "refund" in description:
            suggested_reply = (
                "Hi, thank you for contacting us. "
                "I’m sorry to hear that you’re requesting a refund. "
                "We’ll review your order details and get back to you with the next steps."
            )

        elif (
            "shipping" in title
            or "shipping" in description
            or "delivery" in title
            or "delivery" in description
        ):
            suggested_reply = (
                "Hi, thank you for reaching out. "
                "I’m sorry for the shipping or delivery issue. "
                "We’ll check the order status and provide an update as soon as possible."
            )

        return Response(
            {
                "ticket_id": ticket.id,
                "suggested_reply": suggested_reply,
            }
        )


class TicketCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_ticket(self):
        return get_object_or_404(
            Ticket,
            pk=self.kwargs["pk"],
            owner=self.request.user,
        )

    def get_queryset(self):
        ticket = self.get_ticket()

        return TicketComment.objects.filter(
            ticket=ticket,
            owner=self.request.user,
        )

    def perform_create(self, serializer):
        ticket = self.get_ticket()

        serializer.save(
            ticket=ticket,
            owner=self.request.user,
        )