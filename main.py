# Step 3: make a function so you only have to write the same code once
# Topics info
# - functions: https://www.w3schools.com/python/python_functions.asp

## EXAMPLE: function which finishes emperor's new groove quotes

def quote_finisher(first_word):
    if first_word == 'Im':
        return 'Im… not sure.'
    elif first_word == 'Um':
        return 'Um, I\'ve been turned into a cow. Can I go home?'
    elif first_word == 'Fine':
        return 'Fine. A quick cup of coffee.'
    elif first_word == 'These':
        return 'These were my BEST shoes!'
    else:
        return '~~~ Unrecognized quote ~~~'

# - run `quote_finisher('These')` and try other inputs
# - identify these things about the function: name, arguments, body, return values

## PROBLEM

def ingredient_finder(words, text_body):
    return []
## TODO: fill in this function
## - make the function return a list of words from the `words` argument that are found in text_body
## - call this function a few times on different inputs
