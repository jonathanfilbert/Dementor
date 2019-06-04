from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('get-porto-details/', views.PortoDetails.as_view(), name="portoDetail"),
    path('get-activities/',views.LifeDetails.as_view(),name="activities")
]

urlpatterns = format_suffix_patterns(urlpatterns)