from data import ingredients, effects

total = 0
valid = 0

with open("all_2combos", "w") as output_2combos_file:
    for x in range(0, len(effects)):
        for y in range(x + 1, len(effects)):
            if x >= y:
                continue
            total += 1
            intersection = effects[x].intersection(effects[y])
            if len(intersection) == 0:
                continue
            else:
                valid += 1
                output_2combos_file.write(ingredients[x] + " + " + ingredients[y] + "\n")
                output_2combos_file.write(", ".join(intersection))
                output_2combos_file.write("\n" + str(len(intersection)))
            output_2combos_file.write("\n\n")
    output_2combos_file.write(str(valid) + " valid mixes\n")
    output_2combos_file.write(str(total) + " total combinations")
