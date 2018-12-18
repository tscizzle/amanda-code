# Step 2: check if multiple target words are in text body
# Topics info
# - arrays: https://www.w3schools.com/python/python_arrays.asp
# - for loops: https://www.w3schools.com/python/python_arrays.asp (scroll down to "Looping Array Elements")

## EXAMPLE: check if any ages in an array are senior citizens

SENIOR_CITIZEN_AGE = 65

citizen_ages = [13, 5, 28, 29, 72, 8]

found_a_senior_citizen = False

for age in citizen_ages:

    if age >= SENIOR_CITIZEN_AGE:
        found_a_senior_citizen = True

## PROBLEM

# target words
bad_ingredient_1 = 'Capric/Caprylic Triglycerides (Coconut Oil)'
bad_ingredient_2 = 'Cocos Nucifera (Coconut) Fruit Extract'
bad_ingredient_3 = 'Cocos Nucifera (Coconut) Water'
bad_ingredient_4 = 'Cocos Nucifera (Coconut) Oil'
bad_ingredients = []
## TODO: fill out the array bad_ingredients to replace the individual variables

# text body
ingredients_string = ''
## TODO: replace this line
## assign ingredients_string to the comma-separated list of ingredients

# result
ingredient_found = False
if bad_ingredient_1 in ingredients_string:
    ingredient_found = True
if bad_ingredient_2 in ingredients_string:
    ingredient_found = True
if bad_ingredient_3 in ingredients_string:
    ingredient_found = True
if bad_ingredient_4 in ingredients_string:
    ingredient_found = True
## TODO: replace these lines, to use the array bad_ingredients instead of handling each individual variable
## - loop through the array bad_ingredients
##   - for each ingredient, if the ingredient is in the text body then set ingredient_found to True

print('Ingredient Found:', ingredient_found)
