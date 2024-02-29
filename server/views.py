import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
import os
from dotenv import load_dotenv

from tenacity import retry, stop_after_attempt, wait_exponential

# Configure a proper logging setup using a library like logging
logger = logging.getLogger(__name__)
# Load environment variables from .env file
load_dotenv() 

@api_view(['GET'])
def get_bus_details(request):

    url_gtfs_realtime = 'http://external.chalo.com/dashboard/enterprise/v1/vehicle/sessionData/thiruvananthapuram/ksrtc?vehicleId=KS3132'
    print("***********************Received request for GTFS realtime data*************************")
    headers = {
        'externalauth': 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }
    try:
        response = requests.get(url_gtfs_realtime, headers=headers)
        print('Responsde Content:', response.content)
        print('Response Status:', response.status_code)
        print('Response Headers:', response.headers)
        print('Response Text:', response.text)
        print('Response JSON:', response.request)
    except Exception as e: 
        print("*******************An error occurred: {e}*************************") 
        return Response({'error': 'An error occurred'}, status=500)
