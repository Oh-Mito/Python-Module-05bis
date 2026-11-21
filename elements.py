#!/usr/bin/env python3

def create_fire() -> str:
    return "Fire element created"


def create_water() -> str:
    return "Water element created"


def main() -> None:
    print(f"{create_fire()}")
    print(f"{create_water()}")


if __name__ == "__main__":
    main()
