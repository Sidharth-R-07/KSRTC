

from django.urls import path, include

from rest_framework import routers

from .views import get_bus_details

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-bus-details/', get_bus_details, name='get_bus_details')
]


urlpatterns += router.urls