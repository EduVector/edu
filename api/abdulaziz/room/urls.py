from django.urls import path
from .views import RoomListView

urlpatterns= [
    path('room_list/', RoomListView.as_view(), name='room_list')
]