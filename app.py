"""Command-line entry point for the multibranch practice application."""

import argparse

from src.greeting import create_greeting


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("name", nargs="?", default="DevOps learner")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(create_greeting(args.name))


if __name__ == "__main__":
    main()

