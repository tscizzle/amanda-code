# Step 1: check if target word is in text body
# Topics info
# - running your code: in Terminal, type "python main.py" and hit Enter
# - variables: https://www.w3schools.com/python/python_variables.asp
# - strings: https://www.w3schools.com/python/python_strings.asp
# - booleans: https://www.pythonforbeginners.com/basics/boolean
# - `in` operator (membership): https://www.tutorialspoint.com/python/membership_operators_example.htm
# - print function: https://docs.python.org/3/whatsnew/3.0.html#print-is-a-function

## EXAMPLE: check if a potion includes llama
# - type `python` into the Terminal to open the python interpreter where you can run python commands
# - run these commands in the python interpreter

potion_1 = "baking powder, extract of llama, m&m's"
potion_2 = "extract of cow, sugar, flour, can-go-home-juice"

potion_1_has_llama = 'llama' in potion_1
potion_2_has_llama = 'llama' in potion_2

# type `potion_1_has_llama` and `potion_2_has_llama` to see their values

## PROBLEM

# target word
bad_ingredient = ''
## TODO: replace this line
## assign bad_ingredient to the ingredient you're looking for

# text body
ingredients_string = ''
## TODO: replace this line
## assign ingredients_string to the comma-separated list of ingredients

# result
ingredient_found = None
## TODO: replace this line
## assign the value of ingredient_found based on bad_ingredient and ingredients_string
## - assign ingredient_found to False if ingredients_string does not contain bad_ingredient
## - assign ingredient_found to True if ingredients_string contains bad_ingredient

print('Ingredient Found:', ingredient_found)
