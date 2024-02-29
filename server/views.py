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
    """
    Fetches GTFS realtime bus data from the external API and returns it as a response.

    Handles API requests, fetches GTFS realtime data, and returns a success response with the data or
    an error response if unsuccessful. Implements retry logic with exponential backoff for improved reliability.

    Returns:
        Response object containing GTFS realtime data (on success) or an error message (on failure).
    """

    url_gtfs_realtime = 'https://external.chalo.com/dashboard/gtfs/realtime/thiruvananthapuram/ksrtc/bus'
    print("***********************Received request for GTFS realtime data*************************")

    # Read authentication token from a secure source (e.g., environment variable)
    try:
        externalauth = os.environ['EXTERNAL_AUTH_TOKEN']
    except KeyError:
        logger.error("Missing environment variable EXTERNAL_AUTH_TOKEN")
        return Response({'error': 'Authentication failed'}, status=401)

    headers = {
        'externalauth': externalauth
    }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),  # Configure retry attempts and delays
        retry=requests.exceptions.RequestException  # Retry on any request exceptions
    )
    def fetch_gtfs_data():
        response = requests.get(url_gtfs_realtime, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()

    try:
        gtfs_realtime_data = fetch_gtfs_data()
        logger.info("Successfully fetched GTFS realtime data")
        return Response(gtfs_realtime_data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch GTFS realtime data: {e}")
        return Response({'error': 'Failed to fetch data'}, status=500)
    except ValueError as ve:
        logger.error(f"Failed to parse response as JSON: {ve}")
        return Response({'error': 'Invalid JSON response'}, status=500)
