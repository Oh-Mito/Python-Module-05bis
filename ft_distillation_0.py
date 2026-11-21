from alchemy import potions


def main() -> None:
    print(
        "=== Distillation 0 ===\n"
        "Direct access to alchemy/potions.py"
    )
    print(
        f"Testing strength_potion: {potions.strength_potion()}\n"
        f"Testing healing_potion: {potions.healing_potion()}"
    )


if __name__ == "__main__":
    main()
