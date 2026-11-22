from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:

    allowed_ingdients_list = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    for f in allowed_ingdients_list:
        if f in lower_ingredients:
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
