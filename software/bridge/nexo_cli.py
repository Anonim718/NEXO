"""Simple interactive CLI for the NEXO serial bridge."""

from __future__ import annotations

import argparse

from serial_bridge import NexoBridge


def main() -> None:
    parser = argparse.ArgumentParser(description="Control NEXO over USB serial")
    parser.add_argument("port", help="Serial port, e.g. COM3")
    parser.add_argument("--baud", type=int, default=115200)
    args = parser.parse_args()

    bridge = NexoBridge(args.port, baudrate=args.baud)

    try:
        bridge.connect()
        print("NEXO connected. Type commands or 'quit'.")

        while True:
            command = input("NEXO> ").strip()
            if command.lower() in {"quit", "exit"}:
                break

            try:
                print(bridge.send_command(command))
            except (RuntimeError, TimeoutError, ValueError) as exc:
                print(f"ERROR: {exc}")
    except KeyboardInterrupt:
        print("\nDisconnected.")
    finally:
        bridge.close()


if __name__ == "__main__":
    main()
