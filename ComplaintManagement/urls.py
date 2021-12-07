from django.urls import path
from .views import (
    CreateGrievanceView, CountGrievanceView)

urlpatterns = [
    path('create/', CreateGrievanceView.as_view(), name='create_grievance'),
    path('count/', CountGrievanceView.as_view(), name='count_grievance'),
]
