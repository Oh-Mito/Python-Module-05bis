def validate_ingredients(ingredients: str) -> str:

    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingdients_list = light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()
    for f in allowed_ingdients_list:
        if f in lower_ingredients:
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
