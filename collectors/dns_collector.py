"""DNS enumeration collector."""
import dns.resolver
import dns.rdatatype
import time
from typing import Dict, Any, List, Optional
from utils.logger import setup_logger

logger = setup_logger(__name__)


class DNSCollector:
    """Enumerate DNS records for domains."""

    RECORD_TYPES = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']

    def __init__(
            self,
            timeout: int = 5,
            retries: int = 2,
            rate_limit_delay: float = 0.1):
        self.timeout = timeout
        self.retries = retries
        self.rate_limit_delay = rate_limit_delay
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = timeout
        self.resolver.lifetime = timeout

    def lookup(self, domain: str,
               record_types: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Enumerate DNS records for domain.
        Returns dictionary with DNS data for each record type.
        """
        if record_types is None:
            record_types = self.RECORD_TYPES

        logger.info(f"Starting DNS enumeration for {domain}")
        dns_data = {'domain': domain, 'records': {}}

        for record_type in record_types:
            time.sleep(self.rate_limit_delay)
            dns_data['records'][record_type] = self._query_record(
                domain, record_type)

        logger.info(f"DNS enumeration completed for {domain}")
        return dns_data

    def _query_record(self, domain: str, record_type: str) -> Dict[str, Any]:
        """Query a specific DNS record type."""
        try:
            logger.debug(f"Querying {record_type} records for {domain}")
            answers = self.resolver.resolve(domain, record_type)

            records = []
            for rdata in answers:
                records.append(str(rdata))

            return {
                'type': record_type,
                'records': records,
                'status': 'success'
            }

        except dns.resolver.NXDOMAIN:
            return {
                'type': record_type,
                'records': [],
                'status': 'nxdomain',
                'error': 'Domain does not exist'
            }

        except dns.resolver.NoAnswer:
            return {
                'type': record_type,
                'records': [],
                'status': 'no_answer',
                'error': f'No {record_type} records found'
            }

        except dns.exception.Timeout:
            return {
                'type': record_type,
                'records': [],
                'status': 'timeout',
                'error': 'DNS query timed out'
            }

        except Exception as e:
            logger.error(
                f"DNS query failed for {domain} ({record_type}): {str(e)}")
            return {
                'type': record_type,
                'records': [],
                'status': 'failed',
                'error': str(e)
            }

    def reverse_lookup(self, ip_address: str) -> Dict[str, Any]:
        """
        Perform reverse DNS lookup for IP address.
        """
        try:
            logger.info(f"Performing reverse DNS lookup for {ip_address}")
            addr = dns.reversename.from_address(ip_address)
            result = self.resolver.resolve(addr, "PTR")

            hostnames = [str(rdata) for rdata in result]
            logger.info(f"Reverse DNS lookup successful for {ip_address}")

            return {
                'ip_address': ip_address,
                'hostnames': hostnames,
                'status': 'success'
            }

        except dns.resolver.NXDOMAIN:
            return {
                'ip_address': ip_address,
                'hostnames': [],
                'status': 'not_found',
                'error': 'No reverse DNS records found'
            }

        except Exception as e:
            logger.error(
                f"Reverse DNS lookup failed for {ip_address}: {str(e)}")
            return {
                'ip_address': ip_address,
                'hostnames': [],
                'status': 'failed',
                'error': str(e)
            }
