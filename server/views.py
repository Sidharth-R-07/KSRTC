from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def get_bus_details(request):
    url_gtfs_realtime = 'https://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus'
    headers = {
        'externalauth': 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }
    try:
        print("GET DATA CALLED-------------------")
        response = requests.get(url_gtfs_realtime, headers=headers, timeout=10)
        print('RESPONSE ::------------------- ',response.status_code)
        print('DATA ::',response._content)
        return JsonResponse(response._content)
    except Exception as e:
        # Log the error
        print('ERROR :::    {e}')
        # Return an appropriate error response
        return JsonResponse({'error': 'An error occurred while fetching bus details'}, status=500)
