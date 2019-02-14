import sys
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

########################################################################
def read_str(text, n_lemmas=3):
    '''This function takes in a string. It makes all words lowercase,
       removes stop words, and performs lemmatization. It then prints
       a report including the number of words, sentences, and a list of
       unique words.'''

    # Tokenize user input
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Extract puntuation
    punctuation = [',', '.', '!', '?', "'", ':', '...']
    no_punct = [w for w in words if w not in punctuation]

    # Make lowercase and remove stop words
    lower_words = [w.lower() for w in no_punct]
    no_stops = [w for w in lower_words if w not in stopwords.words('english')]

    # Perform lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(t) for t in no_stops]

    # Get most frequent unique lemmas
    unique_lemmas = list(set(lemmatized))
    lemma_count = Counter(lemmatized).most_common(n_lemmas)

    print("---------------------------------------")
    print("             Input summary:")
    print("---------------------------------------")
    print(" - Number of sentences:            ", len(sentences))
    print(" - Number of words:                ", len(words))
    print(" - Number of words (no stop words):", len(no_stops))
    print(" - Number of unique lemmas:        ", len(unique_lemmas))
    print(" - Most common lemmas:")
    for lemma in lemma_count:
        print("   *", lemma)

#########################################################################
