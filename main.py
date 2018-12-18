# Step 3: make a function so you only have to write the same code once

def ingredient_finder(words, text_body):
    found_words = []
    for word in words:
        if word in text_body:
            found_words.append(word)
    return found_words

print(ingredient_finder(['hello', 'oohba'], 'oohba dooba'))
# prints 'oohba'
