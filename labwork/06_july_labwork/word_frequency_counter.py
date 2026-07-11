# Take a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary
word_count = {}

# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the dictionary
print("\nWord Frequency:")
print(word_count)

# -----------------------------
# Find the most frequent word
# -----------------------------
highest_word = max(word_count, key=word_count.get)

print("\nMost Frequent Word:")
print(highest_word, ":", word_count[highest_word])

# -----------------------------
# Display words in alphabetical order
# -----------------------------
print("\nWords in Alphabetical Order:")

for word in sorted(word_count):
    print(word, ":", word_count[word])