from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    judgement = validate_ingredients(ingredients)
    if "INVALID" in judgement:
        return (f"Spell don't recorded: {spell_name} ({judgement})")
    else:
        return (f"Spell recorded: {spell_name} ({judgement})")
