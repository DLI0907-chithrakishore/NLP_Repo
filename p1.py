custom_stop_words = {'hi','dear','sir','mam','madam', 'thank','thanks','thank you','thanks & regards','please','team', 'pls', 'thank'}
# Update stop words with custom stop words 
updated_stop_words = stop_words.union(custom_stop_words) 
print("Updated Stop Words:",updated_stop_words)

# Function to remove updated stop words from text
def remove_common_words(text, stop_words):
    if not isinstance(text, str):
        return text  # Return the original value if it's not a string
    words = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)


# Function to remove words longer than 20 letters from text 
def remove_long_words(text, max_length=20): 
    # Tokenize the text and convert to lowercase 
    words = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation))) 
    # Filter out words longer than max_length
    filtered_words = [word for word in words if len(word) <= max_length] 
    # Join the filtered words back into a single string 
    return ' '' '.join(filtered_words)
