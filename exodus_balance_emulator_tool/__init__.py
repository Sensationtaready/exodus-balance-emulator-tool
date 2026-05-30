"""Exodus Fake Balance Emulator Tool - Core functionality."""

from .emulator import ExodusEmulator
from .utils import validate_address

__all__ = ["ExodusEmulator", "validate_address"]
__version__ = "0.1.0"