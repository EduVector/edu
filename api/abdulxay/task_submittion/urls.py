from django.urls import path
from .views import TaskSubmittionListView

urlpatterns = [
    path('tasksubmittion_list/', TaskSubmittionListView.as_view(), name='tasksubmittion_list')
]