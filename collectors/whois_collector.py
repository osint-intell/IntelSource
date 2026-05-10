"""WHOIS data collector for domains and IP addresses."""
import whois
from typing import Dict, Any, Optional
from utils.logger import setup_logger

logger = setup_logger(__name__)


class WHOISCollector:
    """Retrieve WHOIS information for domains and IP addresses."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def lookup(self, target: str) -> Dict[str, Any]:
        """
        Perform WHOIS lookup for target (domain or IP).
        Returns dictionary with WHOIS data.
        """
        try:
            logger.info(f"Performing WHOIS lookup for {target}")
            result = whois.whois(target, timeout=self.timeout)

            whois_data = {
                'domain': target,
                'registrar': result.registrar,
                'creation_date': str(
                    result.creation_date) if result.creation_date else None,
                'expiration_date': str(
                    result.expiration_date) if result.expiration_date else None,
                'updated_date': str(
                    result.updated_date) if result.updated_date else None,
                'name_servers': result.name_servers if result.name_servers else [],
                'registrant_country': result.country if result.country else None,
                'status': result.status if result.status else [],
                'raw_data': str(result)}

            logger.info(f"Successfully retrieved WHOIS data for {target}")
            return whois_data

        except Exception as e:
            logger.error(f"WHOIS lookup failed for {target}: {str(e)}")
            return {
                'domain': target,
                'error': str(e),
                'status': 'failed'
            }
