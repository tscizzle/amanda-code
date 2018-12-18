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
bad_ingredients = []
## TODO: replace this line
## assign bad_ingredients to an array of the ingredients you're looking for

# text body
ingredients_string = ''
## TODO: replace this line
## assign ingredients_string to the comma-separated list of ingredients

# result
ingredient_found = None
## TODO: replace this line
## assign the value of ingredient_found based on bad_ingredients and ingredients_string
## - loop through the array bad_ingredients
##   - for each ingredient, if the ingredient is in the text body then set ingredient_found to False

print('Ingredient Found:', ingredient_found)
