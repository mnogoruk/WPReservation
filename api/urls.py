from .views import CabinetListCreateView, ReservationRetrieveView, WorkspaceListCreateView, ReservationCreateView
from django.urls import include, path

urlpatterns = [
    path('cabinet/', CabinetListCreateView.as_view()),
    path('workspace/<int:cabinet>/', WorkspaceListCreateView.as_view()),
    path('workspace/', WorkspaceListCreateView.as_view()),
    path('reservation/', ReservationCreateView.as_view()),
]
