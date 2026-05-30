"""Core emulator logic for generating fake Exodus wallet balances."""

import random
import time
from typing import Dict, Optional
from .utils import validate_address

class ExodusEmulator:
    """Emulates fake balances for Exodus wallet addresses."""

    SUPPORTED_COINS = ["BTC", "ETH", "SOL", "ADA", "XRP"]

    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def generate_balance(self, address: str, coin: str = "BTC") -> Dict[str, float]:
        """Generate a fake balance for the given address and coin."""
        if not validate_address(address):
            raise ValueError("Invalid address format")
        if coin not in self.SUPPORTED_COINS:
            raise ValueError(f"Unsupported coin: {coin}")

        balance = round(random.uniform(0.001, 100.0), 8)
        return {
            "address": address,
            "coin": coin,
            "balance": balance,
            "timestamp": int(time.time())
        }