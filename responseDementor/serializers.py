from rest_framework import serializers
from .models import PortofolioData,WhatAmIDoing

class PortofolioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortofolioData
        fields = ("title","category","short_description","description","image")

class WhatAmIDoingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatAmIDoing
        fields = ("time","update")