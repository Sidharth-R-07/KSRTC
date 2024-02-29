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
        response = requests.get(url_gtfs_realtime, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        print(f'Data:', data)
        # Process data as needed
        return JsonResponse(data)  # Return the fetched data as a JSON response
    except Exception as e:
        # Log the error
        print(f"An error occurred: {e}")
        # Return an appropriate error response
        return JsonResponse({'error': 'An error occurred while fetching bus details'}, status=500)
