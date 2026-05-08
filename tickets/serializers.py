from rest_framework import serializers

from organizations.models import Organization
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'title',
            'description',
            'status',
            'priority',
            'organization',
            'owner',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
        ]

    def validate_organization(self, organization):
        request = self.context.get('request')

        if organization.owner != request.user:
            raise serializers.ValidationError(
                'You can only create tickets for your own organizations.'
            )

        return organization