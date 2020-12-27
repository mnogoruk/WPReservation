from .views import CabinetListCreateView, ReservationRetrieveView, WorkspaceListCreateView, ReservationCreateView, WorkspaceRetrieveView
from django.urls import include, path

urlpatterns = [
    path('cabinet/', CabinetListCreateView.as_view()),
    path('workspace/<int:pk>/', WorkspaceRetrieveView.as_view()),
    path('workspace/', WorkspaceListCreateView.as_view()),
    path('reservation/', ReservationCreateView.as_view()),
]
