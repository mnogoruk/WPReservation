from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Cabinet, Workspace, WorkspaceReservation
from .serializer import CabinetSerializer, WorkspaceSerializer, WorkspaceReservationSerializer


# Create your views here.

class CabinetListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class CabinetUpdateRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CabinetSerializer


class WorkspaceListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        cabinet_id = self.kwargs.get('cabinet')
        if cabinet_id is None:
            workspaces = Workspace.objects.all()
        else:
            workspaces = Workspace.objects.filter(cabinet_id=cabinet_id)
        return workspaces


class WorkspaceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WorkspaceSerializer


class ReservationCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkspaceReservationSerializer

    def create(self, request, *args, **kwargs):
        print(kwargs)
        print(args)
        print(request.POST)


class ReservationRetrieveView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WorkspaceReservationSerializer
