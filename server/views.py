import requests
from rest_framework.decorators import api_view


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
