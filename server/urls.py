
from .views import  get_bus_details
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('getData/', get_bus_details, name='getData')
]


urlpatterns += router.urls