from rest_framework.serializers import ModelSerializer
from .models import Cabinet, Workspace, WorkspaceReservation


class CabinetSerializer(ModelSerializer):
    class Meta:
        model = Cabinet


class WorkspaceSerializer(ModelSerializer):
    class Meta:
        model = Workspace


class WorkspaceReservationSerializer(ModelSerializer):
    class Meta:
        model = WorkspaceReservation
