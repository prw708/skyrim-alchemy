import re

all_ingredients = []
all_effects = []

with open("Skyrim_Ingredients_Table_Only", "r") as input_file:
    for line in input_file:
        ingredient = re.search("^<td rowspan=\"2\"><a ([^>]+)+>([^<]+)</a>", line)
        effect = re.search("<td class=\"(EffectPos|EffectNeg)\"><a href=\"(\S+)\" title=\"([^\"]+)\">(.*)</td>$", line)
        if ingredient != None:
            all_ingredients.append(ingredient.group(2))
        if effect != None:
            all_effects.append(effect.group(3))

with open("all_ingredients", "w") as output_ingredients_file:
    for ingredient in all_ingredients:
        output_ingredients_file.write(ingredient)
        output_ingredients_file.write("\n")

counter = 1
with open("all_effects", "w") as output_effects_file:
    for effect in all_effects:
        output_effects_file.write(effect)
        if counter % 4 == 0:
            output_effects_file.write("\n")
        else:
            output_effects_file.write(",")
        counter += 1
            
