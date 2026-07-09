# Function to count vowels
def count_vowels(text):
    count = 0
    # Check each character
    for ch in text:
        # Convert to lowercase and check if it is a vowel
        if ch.lower() in "aeiou":
            count += 1
    return count

# Main Program
sentence = input("Enter a sentence: ")
total = count_vowels(sentence)
print("Total Vowels:", total)