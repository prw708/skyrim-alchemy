# Skyrim Alchemy
Python scripts that finds all combinations of possible potions and poisons in Skyrim.

## Explanation
In Skyrim, you can mix 2 or 3 ingredients found in the world together. Each ingredient has 4 effects. If any of the 4 effects are shared by these ingredients, a successful potion or poison is created.

## Tasks
1. Parse ingredient list and effects list from the UESP webpage HTML and convert it into CSV files 
2. Read all ingredients and all effects from CSV files
2. Loop through all possible combinations of 2
3. Loop through all possible combinations of 3
3. If intersection of ingredients' effects is not empty, save it as a possible potion/poison

## Results
There are 113 ingredients in Skyrim.
A total of 6328 combinations of 2 are possible. Out of those, 1814 are valid potion/poison mixes.
A total of 234136 combinations of 3 are possible. Out of those, 151703 are valid potion/poison mixes.

The maximum effects possible are a few 5-effect mixes, a few of them are:

Ancestor Moth Wing + Bone Meal + Spawn Ash
Fortify Conjuration, Ravage Stamina, Damage Stamina, Resist Fire, Fortify Enchanting

Bear Claws + Eye of Sabre Cat + Hanging Moss
Fortify One-handed, Restore Stamina, Fortify Health, Damage Magicka Regen, Damage Magicka

Blisterwort + Human Heart + Jarrin Root
Frenzy, Damage Stamina, Damage Magicka Regen, Damage Health, Damage Magicka

Creep Cluster + Mora Tapinella + Scaly Pholiota
Fortify Carry Weight, Restore Magicka, Fortify Illusion, Weakness to Magic, Regenerate Stamina

Daedra Heart + Eye of Sabre Cat + Silverside Perch
Restore Health, Ravage Health, Restore Stamina, Damage Stamina Regen, Damage Magicka

Glow Dust + Glowing Mushroom + Hanging Moss
Resist Shock, Fortify Destruction, Fortify Health, Damage Magicka Regen, Damage Magicka

## References
The ingredient list has been documented by the [Unofficial Elder Scrolls Pages](http://en.uesp.net/wiki/Skyrim:Ingredients).

