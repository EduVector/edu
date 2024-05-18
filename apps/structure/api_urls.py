from django.urls import path, include

urlpatterns = [
    path('', include('api.abdulaziz.room.urls')),
    path('', include('api.abdulxay.payment.urls')),
    path('', include('api.abdulxay.task_submittion.urls')),
    path('', include('api.abdulxay.task.urls')),
    path('', include('api.abdulxay.attendance.urls')),
]