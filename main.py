# Step 2: check if multiple target words are in text body
# Topics info
# - arrays: https://www.w3schools.com/python/python_arrays.asp
# - for loops: https://www.w3schools.com/python/python_arrays.asp (scroll down to "Looping Array Elements")

## EXAMPLE 1 (Arrays): You have a list of credit card numbers. Check if any of them match your credit card number.

THE_NUMBER = 8

possible_card_numbers = [13, 5, 28, 8, 29, 72]

found_my_credit_card_number = False

for number in possible_card_numbers:

    if possible_card_numbers == THE_NUMBER:
        # The number is... 8.
        found_my_credit_card_number = True

## EXAMPLE 2 (For loops): Figure out whether or not someone is in their late twenties.
list_of_ages = [3, 26, 73, 31, 55, 66, 28, 16]

for age in list_of_ages:
    print("What is he, in his late twenties?")
    if age < 25:
        print("I'm... not sure.")
    elif age > 30:
        print("I'm... not sure.")
    else:
        print("Yes.")

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
