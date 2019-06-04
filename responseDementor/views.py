from django.http import HttpResponse
from .models import PortofolioData,WhatAmIDoing
from .serializers import PortofolioDataSerializer,WhatAmIDoingSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class PortoDetails(APIView):
    def get(self,request):
        portos = PortofolioData.objects.all()
        serialized = PortofolioDataSerializer(portos,many=True)
        return Response(serialized.data)
    
    def post(self,request):
        return HttpResponse("POST is not supported")

class LifeDetails(APIView):
    def get(self,request):
        activities = WhatAmIDoing.objects.all()
        activitiesSerialized = WhatAmIDoingSerializer(activities,many=True)
        return Response(activitiesSerialized.data)
    
    def post(self,request):
        return HttpResponse("POST is not supported")
