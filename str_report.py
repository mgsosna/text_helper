# Load libraries
import sys
from nltk import word_tokenize, sent_tokenize

# If user doesn't input anything, tell them to write something
if len(sys.argv) < 2:
    print("Oops - don't forget to input some text!")
    quit()

# Tokenize user input
sentences = sent_tokenize(sys.argv[1])
words = word_tokenize(sys.argv[1])

# Extract puntuation
punctuation = [',', '.', '!', '?', "'"]
no_punct = [w for w in words if w not in punctuation]

# Get unique words
lower = [w.lower() for w in no_punct]
lower = list(set(lower))

print("-------------------------------")
print("        Input summary:")
print("-------------------------------")
print(" - Number of words:    ", len(no_punct))
print(" - Number of sentences:", len(sentences))
print(" - Unique words:")
for word in lower:
    print("   *", word)
