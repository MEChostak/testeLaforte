# from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Tracking
from .serializers import TrackingSerializer

# Create your views here.
class TrackingViewSet(ModelViewSet):

    serializer_class = TrackingSerializer

    def get_queryset(self):
        queryset = Tracking.objects.all()
        tracking_number = self.request.query_params.get('tracking_number', None)
        if tracking_number is not None:
            queryset = queryset.filter(tracking_number=tracking_number)
        return queryset