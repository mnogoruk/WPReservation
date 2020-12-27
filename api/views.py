from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Cabinet, Workspace
from .serializer import CabinetSerializer, WorkspaceSerializer, WorkspaceReservationSerializer


class CabinetListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class CabinetRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CabinetSerializer

    def get_queryset(self):
        return Cabinet.objects.filter(id=self.kwargs['pk'])


class WorkspaceListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        time_to = self.kwargs['time_to']
        time_from = self.kwargs['time_from']
        if time_to is not None:
            # условие: берём те записи у которых для любого периода сущестующей брони
            # нет пересечения с указнаным периодом
            workspaces = Workspace.objects.filter(~Q(reservation__time_from__range=(time_from, time_to),
                                                     reservation__time_to__range=(time_from, time_to)))

        else:
            workspaces = Workspace.objects.all()
        return workspaces

    def get(self, request, *args, **kwargs):
        time_from = self.request.GET.get('time_from')
        time_to = self.request.GET.get('time_to')

        # смотрим, чтобы либо оба параметра были, либо ни одного

        if not ((time_to is None) ^ (time_from is None)):
            self.kwargs['time_to'] = time_to
            self.kwargs['time_from'] = time_from
            return super().get(request, *args, **kwargs)
        else:
            return Response({'detail': 'both time_from and time_to or not one of them must be specified'},
                            status=status.HTTP_400_BAD_REQUEST)


class WorkspaceRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()


def f(a):
    return a[0]


class ReservationCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkspaceReservationSerializer

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        # анмутим QueryDict
        data = dict(zip(data.keys(), map(f, data.values())))
        data['user_id'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReservationRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = WorkspaceReservationSerializer
