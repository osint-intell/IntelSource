"""Validation utilities for IP addresses and domains."""
import re
import ipaddress
from typing import Tuple


def is_valid_ip(target: str) -> bool:
    """Check if target is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def is_valid_domain(target: str) -> bool:
    """Check if target is a valid domain name."""
    domain_pattern = re.compile(
        r'^(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$',
        re.IGNORECASE
    )
    return bool(domain_pattern.match(target))


def is_valid_email(target: str) -> bool:
    """Check if target is a valid email address."""
    email_pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    return bool(email_pattern.match(target))


def classify_target(target: str) -> Tuple[str, bool]:
    """
    Classify target as IP, domain, or email.
    Returns (target_type, is_valid)
    """
    target = target.strip()

    if is_valid_ip(target):
        return ('ip', True)
    elif is_valid_email(target):
        return ('email', True)
    elif is_valid_domain(target):
        return ('domain', True)
    else:
        return ('unknown', False)
