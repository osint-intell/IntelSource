"""Email MX validation collector."""
import dns.resolver
from typing import Dict, Any, List
from utils.logger import setup_logger

logger = setup_logger(__name__)


class EmailValidator:
    """Validate email addresses by checking MX records."""

    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = timeout

    def validate(self, email: str) -> Dict[str, Any]:
        """
        Validate email by checking MX records for the domain.
        Returns MX records and validation status.
        """
        try:
            if '@' not in email:
                return {
                    'email': email,
                    'status': 'invalid',
                    'error': 'Invalid email format'
                }

            domain = email.split('@')[1].lower()
            logger.info(f"Validating email domain {domain}")

            mx_records = self._get_mx_records(domain)

            if not mx_records:
                return {
                    'email': email,
                    'domain': domain,
                    'mx_records': [],
                    'status': 'no_mx',
                    'error': 'No MX records found'
                }

            logger.info(f"Email validation successful for {email}")
            return {
                'email': email,
                'domain': domain,
                'mx_records': mx_records,
                'status': 'valid'
            }

        except Exception as e:
            logger.error(f"Email validation failed for {email}: {str(e)}")
            return {
                'email': email,
                'status': 'failed',
                'error': str(e)
            }

    def _get_mx_records(self, domain: str) -> List[Dict[str, str]]:
        """Retrieve MX records for domain."""
        try:
            mx_records = []
            answers = self.resolver.resolve(domain, 'MX')

            for rdata in answers:
                mx_records.append({
                    'priority': rdata.preference,
                    'exchange': str(rdata.exchange)
                })

            return sorted(mx_records, key=lambda x: x['priority'])

        except Exception as e:
            logger.error(
                f"Failed to retrieve MX records for {domain}: {
                    str(e)}")
            return []
