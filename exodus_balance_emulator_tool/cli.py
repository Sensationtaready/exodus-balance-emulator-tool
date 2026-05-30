"""Command-line interface for the Exodus balance emulator."""

import argparse
from .emulator import ExodusEmulator

def main():
    parser = argparse.ArgumentParser(description="Exodus Fake Balance Emulator Tool")
    parser.add_argument("--address", required=True, help="Wallet address to emulate")
    parser.add_argument("--coin", default="BTC", help="Cryptocurrency (default: BTC)")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible results")
    args = parser.parse_args()

    emulator = ExodusEmulator(seed=args.seed)
    result = emulator.generate_balance(args.address, args.coin)
    print(f"Generated balance for {result['address']}: {result['balance']} {result['coin']}")

if __name__ == "__main__":
    main()