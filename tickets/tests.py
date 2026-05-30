from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from organizations.models import Organization
from tickets.models import Ticket, TicketComment


User = get_user_model()


class TicketSuggestedReplyTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
            role="admin",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            email="otheruser@example.com",
            password="testpass123",
            role="agent",
        )

        self.organization = Organization.objects.create(
            name="Test Organization",
            description="A test support organization",
            owner=self.user,
        )

        self.ticket = Ticket.objects.create(
            title="Customer cannot access account",
            description="The customer cannot login after resetting password.",
            status="open",
            priority="high",
            organization=self.organization,
            owner=self.user,
        )

    def test_authenticated_user_can_get_suggested_reply_for_own_ticket(self):
        self.client.force_authenticate(user=self.user)

        url = reverse(
            "ticket-suggested-reply",
            kwargs={"pk": self.ticket.pk},
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ticket_id"], self.ticket.id)
        self.assertIn(
            "having trouble accessing your account",
            response.data["suggested_reply"],
        )

    def test_user_cannot_get_suggested_reply_for_another_users_ticket(self):
        self.client.force_authenticate(user=self.other_user)

        url = reverse(
            "ticket-suggested-reply",
            kwargs={"pk": self.ticket.pk},
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_user_cannot_get_suggested_reply(self):
        url = reverse(
            "ticket-suggested-reply",
            kwargs={"pk": self.ticket.pk},
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TicketCommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="commentuser",
            email="commentuser@example.com",
            password="testpass123",
            role="admin",
        )

        self.other_user = User.objects.create_user(
            username="othercommentuser",
            email="othercommentuser@example.com",
            password="testpass123",
            role="agent",
        )

        self.organization = Organization.objects.create(
            name="Comment Test Organization",
            description="A test organization for ticket comments",
            owner=self.user,
        )

        self.ticket = Ticket.objects.create(
            title="Customer cannot access account",
            description="The customer cannot login after resetting password.",
            status="open",
            priority="high",
            organization=self.organization,
            owner=self.user,
        )

        self.comment = TicketComment.objects.create(
            ticket=self.ticket,
            owner=self.user,
            body="Customer already tried resetting the password.",
            is_internal=True,
        )

    def test_authenticated_user_can_list_comments_for_own_ticket(self):
        self.client.force_authenticate(user=self.user)

        url = reverse(
            "ticket-comment-list-create",
            kwargs={"pk": self.ticket.pk},
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]["body"],
            "Customer already tried resetting the password.",
        )

    def test_authenticated_user_can_create_comment_for_own_ticket(self):
        self.client.force_authenticate(user=self.user)

        url = reverse(
            "ticket-comment-list-create",
            kwargs={"pk": self.ticket.pk},
        )

        payload = {
            "body": "Need to verify whether the account is locked.",
            "is_internal": True,
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["ticket"], self.ticket.id)
        self.assertEqual(response.data["owner"], self.user.id)
        self.assertEqual(
            response.data["body"],
            "Need to verify whether the account is locked.",
        )
        self.assertTrue(response.data["is_internal"])

    def test_user_cannot_list_comments_for_another_users_ticket(self):
        self.client.force_authenticate(user=self.other_user)

        url = reverse(
            "ticket-comment-list-create",
            kwargs={"pk": self.ticket.pk},
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_create_comment_for_another_users_ticket(self):
        self.client.force_authenticate(user=self.other_user)

        url = reverse(
            "ticket-comment-list-create",
            kwargs={"pk": self.ticket.pk},
        )

        payload = {
            "body": "Trying to comment on another user's ticket.",
            "is_internal": True,
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_user_cannot_list_comments(self):
        url = reverse(
            "ticket-comment-list-create",
            kwargs={"pk": self.ticket.pk},
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_user_cannot_create_comment(self):
        url = reverse(
            "ticket-comment-list-create",
            kwargs={"pk": self.ticket.pk},
        )

        payload = {
            "body": "Unauthenticated comment attempt.",
            "is_internal": True,
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)