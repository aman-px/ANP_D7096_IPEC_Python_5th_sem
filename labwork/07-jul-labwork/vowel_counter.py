def count_vowels(text):
    """Count vowels in a string irrespective of case."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


# Main program
sentence = input("Enter a sentence: ")
result = count_vowels(sentence)
print("Total Vowels:", result)
