# Step 1: check if target word is in text body

# target word
bad_ingredient = 'Cocos Nucifera (Coconut) Oil'

# text body
ingredients_string = 'Water / Eau (Aqua), Cetyl Alcohol, Cetrimonium Chloride, Behentrimonium Chloride, Isopropyl Palmitate, Glycerin, Cyclopentasiloxane, Fragrance / Parfum, Keratin Amino Acids, Cocoyl Hydrolyzed Keratin, Keratin, Hydrolyzed Keratin, Hydrolyzed Collagen, Butyrospermum Parkii (Shea) Butter, Olea Europaea (Olive) Fruit Oil, Cocos Nucifera (Coconut) Oil, Sesamum Indicum (Sesame) Seed Oil, Simmondsia Chinensis (Jojoba) Seed Oil, Hydrolyzed Corn Protein, Hydrolyzed Soy Protein, Dimethicone, Panthenol (Vitamin B5), Phenoxyethanol, Citric Acid, Polyquaternium-55, Stearyl Alcohol'

# result
ingredient_found = bad_ingredient in ingredients_string

print('Ingredient Found:', ingredient_found)
