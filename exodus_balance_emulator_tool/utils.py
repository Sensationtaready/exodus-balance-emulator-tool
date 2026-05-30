"""Utility functions for the Exodus emulator tool."""

import re

def validate_address(address: str) -> bool:
    """Basic validation for cryptocurrency addresses."""
    if not address:
        return False

    # Simple regex patterns for different coins (not production-grade)
    patterns = {
        "BTC": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        "ETH": r"^0x[a-fA-F0-9]{40}$",
        "SOL": r"^[1-9A-HJ-NP-Za-km-z]{32,44}$",
    }

    for coin, pattern in patterns.items():
        if re.match(pattern, address):
            return True
    return False