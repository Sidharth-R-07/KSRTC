from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def get_bus_details(request):
    url_gtfs_realtime = 'http://external.chalo.com/dashboard/enterprise/v1/vehicle/sessionData/thiruvananthapuram/ksrtc?vehicleId=KS3132'
    headers = {
        'externalauth': 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }
    try:
        print("GET DATA CALLED-------------------")
        response = requests.get(url_gtfs_realtime, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        print('DATA ::------------------- {data}')
        return JsonResponse(data)
    except Exception as e:
        # Log the error
        print('ERROR :::    {e}')
        # Return an appropriate error response
        return JsonResponse({'error': 'An error occurred while fetching bus details'}, status=500)
