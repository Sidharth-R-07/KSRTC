# views.py

from logging import log
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
# @retry(stop_max_attempt_number=3, wait_fixed=2000)  
def get_bus_details(request):
    # URL for GTFS realtime data
    print("get_bus_details")
    
    url_gtfs_realtime = 'http://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus'

    # Headers
    headers = {
        'externalauth': 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }

    # Make GET request for GTFS realtime data
    response = requests.get(url_gtfs_realtime, headers=headers, timeout=10)
    print(response.status_code)
    if response.status_code == 200:
        gtfs_realtime_data = response.json()  # Assuming response is JSON
        print(gtfs_realtime_data)
        return Response(gtfs_realtime_data)
    else:
        print("get_bus_details")
        return Response({'error': 'Failed to fetch data'}, status=500)
