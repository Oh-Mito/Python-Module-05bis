def light_spell_allowed_ingredients() -> list[str]:
    ingredients = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    judgement = validate_ingredients(ingredients)
    return (f"Spell recorded: {spell_name} ({judgement})")


if __name__ == "__main__":
    print(light_spell_allowed_ingredients())
