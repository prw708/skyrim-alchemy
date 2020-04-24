from data import ingredients, effects

total = 0
valid = 0

with open("all_3combos", "w") as output_3combos_file:
    for x in range(0, len(effects)):
        for y in range(x + 1, len(effects)):
            if x >= y:
                continue
            for z in range(x + 2, len(effects)):
                if y >= z:
                    continue
                total += 1
                intersection_xy = effects[x].intersection(effects[y])
                intersection_yz = effects[y].intersection(effects[z])
                intersection_xz = effects[x].intersection(effects[z])
                union_xyz = intersection_xy.union(intersection_yz)
                union_xyz = union_xyz.union(intersection_xz)
                if len(union_xyz) == 0:
                    continue
                else:
                    valid += 1
                    output_3combos_file.write(ingredients[x] + " + " + ingredients[y] + " + " + ingredients[z] + "\n")
                    output_3combos_file.write(", ".join(union_xyz))
                    output_3combos_file.write("\n" + str(len(union_xyz)))
                output_3combos_file.write(" \n\n")
    output_3combos_file.write(str(valid) + " valid mixes\n")
    output_3combos_file.write(str(total) + " total combinations")
