from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Cabinet, Workspace, WorkspaceReservation


class CabinetSerializer(ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class WorkspaceReservationOnlyViewSerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = WorkspaceReservation
        fields = ['time_from', 'time_to', 'user']


class WorkspaceReservationSerializer(ModelSerializer):
    time_to = serializers.DateTimeField()
    time_from = serializers.DateTimeField()
    user_id = serializers.IntegerField()

    class Meta:
        model = WorkspaceReservation
        fields = ['time_to', 'time_from', 'workspace', 'user_id']
        read_only_fields = ['user_id']

    def validate(self, data):

        time_from = data['time_from']
        time_to = data['time_to']
        workspace_id = data['workspace']

        if time_from > time_to:
            raise serializers.ValidationError("time_to must occur after time_from")

        if WorkspaceReservation.objects.filter(
                workspace_id=workspace_id,
                time_from__lt=time_to,
                time_to__gt=time_from).exists():
            raise serializers.ValidationError("there is a reservation for this time")

        return data


class WorkspaceSerializer(ModelSerializer):
    reservation = WorkspaceReservationOnlyViewSerializer(read_only=True, many=True)

    class Meta:
        model = Workspace
        fields = ['id', 'number', 'opt', 'reservation', 'cabinet_id']
