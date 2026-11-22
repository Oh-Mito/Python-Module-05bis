import alchemy.grimoire.light_spellbook


def main() -> None:
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly"
    )
    ret = alchemy.grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire"
    )
    print(f"Testing record light spell: {ret}")


if __name__ == "__main__":
    main()
