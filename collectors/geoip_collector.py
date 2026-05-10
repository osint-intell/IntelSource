"""GeoIP and ASN data collector."""
import os
import requests
import json
from typing import Dict, Any, Optional
from utils.logger import setup_logger

logger = setup_logger(__name__)


class GeoIPCollector:
    """Retrieve GeoIP and ASN information for IP addresses."""

    def __init__(self, api_token: Optional[str] = None):
        self.api_token = api_token or os.getenv('IPINFO_TOKEN')
        self.base_url = "https://ipinfo.io"

    def lookup(self, ip_address: str) -> Dict[str, Any]:
        """
        Lookup GeoIP and ASN data for IP address using ipinfo.io.
        Returns location, ASN, and network information.
        Free tier: 50k requests/month. Sign up at https://ipinfo.io
        """
        try:
            logger.info(f"Performing GeoIP lookup for {ip_address}")

            url = f"{self.base_url}/{ip_address}"
            params = {}
            if self.api_token:
                params['token'] = self.api_token

            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Handle error responses
            if 'error' in data:
                logger.warning(
                    f"ipinfo.io error for {ip_address}: {
                        data.get(
                            'error', {}).get(
                            'message', 'Unknown')}")
                return {
                    'ip_address': ip_address,
                    'status': 'failed',
                    'error': data.get('error', {}).get('message', 'API error')
                }

            # Parse location (lat,lon format)
            loc_parts = data.get('loc', ',').split(',')
            latitude = loc_parts[0] if len(loc_parts) > 0 else None
            longitude = loc_parts[1] if len(loc_parts) > 1 else None

            geoip_data = {
                'ip_address': ip_address,
                'country': data.get('country', 'Unknown'),
                'region': data.get('region', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'latitude': latitude,
                'longitude': longitude,
                'timezone': data.get('timezone', 'Unknown'),
                'isp': data.get('org', 'Unknown'),
                'asn': data.get('asn', 'Unknown'),
                'hostname': data.get('hostname', 'N/A'),
                'status': 'success'
            }

            logger.info(f"GeoIP lookup successful for {ip_address}")
            return geoip_data

        except requests.exceptions.RequestException as e:
            logger.error(f"GeoIP lookup failed for {ip_address}: {str(e)}")
            return {
                'ip_address': ip_address,
                'status': 'failed',
                'error': str(e)
            }

        except json.JSONDecodeError as e:
            logger.error(
                f"Failed to parse GeoIP response for {ip_address}: {
                    str(e)}")
            return {
                'ip_address': ip_address,
                'status': 'failed',
                'error': 'Invalid JSON response'
            }
