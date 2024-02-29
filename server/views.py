import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
import os
from tenacity import retry, stop_after_attempt, wait_exponential

# Configure a proper logging setup using a library like logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_bus_details(request):
    logger.info("Received request for GTFS realtime data")
    """
    Fetches GTFS realtime bus data from the external API and returns it as a response.

    Handles API requests, fetches GTFS realtime data, and returns a success response with the data or
    an error response if unsuccessful. Implements retry logic with exponential backoff for improved reliability.

    Returns:
        Response object containing GTFS realtime data (on success) or an error message (on failure).
    """

    url_gtfs_realtime = 'http://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus'

    # Read authentication token from a secure source (e.g., environment variable)
    try:
        externalauth = os.environ['EXTERNAL_AUTH_TOKEN']
    except KeyError:
        logger.error("Missing environment variable EXTERNAL_AUTH_TOKEN")
        return Response({'error': 'Authentication failed'}, status=401)

    headers = {
        'externalauth': 'RWLXTEgMcmuMj1mehBWi3ROaAfTmQwXjGksxvxD9'
    }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),  # Configure retry attempts and delays
        retry=requests.exceptions.RequestException  # Retry on any request exceptions
    )
    def fetch_gtfs_data():
        response = requests.get(url_gtfs_realtime, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()

    try:
        gtfs_realtime_data = fetch_gtfs_data()
        logger.info("Successfully fetched GTFS realtime data")
        return Response(gtfs_realtime_data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch GTFS realtime data: {e}")
        return Response({'error': 'Failed to fetch data'}, status=500)

