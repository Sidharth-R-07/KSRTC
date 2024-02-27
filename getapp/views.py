# views.py

import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_bus_details(request):
    # URL for GTFS realtime data
    url_gtfs_realtime = 'http://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus'

    # Headers
    headers = {
        'externalauth': 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }

    # Make GET request for GTFS realtime data
    response = requests.get(url_gtfs_realtime, headers=headers)
    if response.status_code == 200:
        gtfs_realtime_data = response.json()  # Assuming response is JSON
        return Response(gtfs_realtime_data)
    else:
        return Response({'error': 'Failed to fetch GTFS realtime data'}, status=500)
