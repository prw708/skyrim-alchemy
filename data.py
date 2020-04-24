ingredients = []
effects = []

with open("all_ingredients", "r") as input_file:
    for line in input_file:
        ingredients.append(line.strip())

with open("all_effects", "r") as input_file:
    for line in input_file:
        effects_set = set(line.strip().split(","))
        effects.append(effects_set)
