from django.urls import path
from .views import AttendanceListView

urlpatterns = [
    path('attendance_list/', AttendanceListView.as_view(), name='attendance_list')
]