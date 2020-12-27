from .views import CabinetListCreateView, ReservationCreateView, WorkspaceListCreateView
from django.urls import include, path

urlpatterns = [
    path('cabinet/', CabinetListCreateView.as_view()),
    path('workspace/<int:cabinet>/', WorkspaceListCreateView.as_view()),
    path('workspace/', WorkspaceListCreateView.as_view()),
    path('reservation/', ReservationCreateView.as_view()),
]
