from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import Complaint
from .serializers import (
    CreateGrievanceSerializer, CountGrievanceSerializer, GrievanceSerializer)

# Create your views here.

class CreateGrievanceView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Complaint.objects.all()
    serializer_class = CreateGrievanceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        complaint = serializer.save()
        complaint_dict = GrievanceSerializer(complaint)
        return Response(complaint_dict.data, status=status.HTTP_201_CREATED)

class CountGrievanceView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Complaint.objects.all()
    serializer_class = CountGrievanceSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        count = serializer.get_count()
        return Response(count, status=status.HTTP_200_OK)

# closed complaints(user)......objects(),filter.()

# register complaints(user)

# pendings complaints(user)
