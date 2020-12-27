from .views import CabinetListCreateView, \
    CabinetRetrieveView, \
    ReservationRetrieveView, \
    WorkspaceListCreateView, \
    ReservationCreateView, \
    WorkspaceRetrieveView

from django.urls import path

urlpatterns = [
    path('cabinet/', CabinetListCreateView.as_view()),
    path('cabinet/<int:pk>/', CabinetRetrieveView.as_view()),
    path('workspace/<int:pk>/', WorkspaceRetrieveView.as_view()),
    path('workspace/', WorkspaceListCreateView.as_view()),
    path('reservation/', ReservationCreateView.as_view()),
    path('reservation/<int:pk>/', ReservationRetrieveView.as_view())
]
