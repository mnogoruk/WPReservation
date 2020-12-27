from rest_framework.serializers import ModelSerializer
from .models import Cabinet, Workspace, WorkspaceReservation


class CabinetSerializer(ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class WorkspaceSerializer(ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'


class WorkspaceReservationSerializer(ModelSerializer):
    class Meta:
        model = WorkspaceReservation
        fields = '__all__'
