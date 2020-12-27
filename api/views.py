from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from .models import Cabinet, Workspace, WorkspaceReservation
from .serializer import CabinetSerializer, WorkspaceSerializer, WorkspaceReservationSerializer


# Create your views here.

class CabinetListCreateView(ListCreateAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class CabinetUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CabinetSerializer


class WorkspaceListCreateView(ListCreateAPIView):
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        cabinet_id = self.kwargs.get('cabinet')
        if cabinet_id is None:
            workspaces = Workspace.objects.all()
        else:
            workspaces = Workspace.objects.filter(cabinet_id=cabinet_id)
        return workspaces


class WorkspaceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkspaceSerializer


class WorkspaceReservationCreateView(CreateAPIView):
    serializer_class = WorkspaceReservationSerializer


class ReservationRetrieveView(RetrieveAPIView):
    serializer_class = WorkspaceReservationSerializer
