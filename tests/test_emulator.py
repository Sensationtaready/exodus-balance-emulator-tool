"""Tests for the Exodus balance emulator."""

import pytest
from exodus_balance_emulator_tool.emulator import ExodusEmulator
from exodus_balance_emulator_tool.utils import validate_address

def test_validate_address():
    assert validate_address("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")  # BTC
    assert validate_address("0x742d35Cc6634C0532925a3b844Bc454e4438f44e")  # ETH
    assert not validate_address("invalid_address")

def test_emulator_generate_balance():
    emulator = ExodusEmulator(seed=42)
    result = emulator.generate_balance("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    assert result["address"] == "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    assert result["coin"] == "BTC"
    assert isinstance(result["balance"], float)

def test_emulator_reproducible():
    emulator1 = ExodusEmulator(seed=123)
    emulator2 = ExodusEmulator(seed=123)
    result1 = emulator1.generate_balance("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    result2 = emulator2.generate_balance("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    assert result1["balance"] == result2["balance"]