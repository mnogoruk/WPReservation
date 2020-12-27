from django.contrib import admin
from .models import Cabinet, Workspace, WorkspaceReservation


admin.site.register(Workspace)
admin.site.register(Cabinet)
admin.site.register(WorkspaceReservation)
