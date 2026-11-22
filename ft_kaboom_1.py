def main() -> None:
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION"
    )
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        ret = dark_spell_record("Fantasy", "bats, FrOGS and arsenic")
        print(f"Testing record dark spell: {ret}")
    except ImportError:
        raise


if __name__ == "__main__":
    main()
