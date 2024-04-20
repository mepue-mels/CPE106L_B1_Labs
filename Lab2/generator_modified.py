"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random

# articles = ("A", "THE")

# nouns = ("BOY", "GIRL", "BAT", "BALL")

# verbs = ("HIT", "SAW", "LIKED")

# prepositions = ("WITH", "BY")

def getWords(filename):
    try:
        f = open(filename, 'r')
        wordList = []
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.strip().split()
            word = line[0]
            wordList.append(word)
        return tuple(wordList)
        
    except:
        print("Invalid filename.")
        raise SystemExit


def sentence(articles, nouns, verbs, prepositions):
    """Builds and returns a sentence."""
    return nounPhrase(articles, nouns) + " " + verbPhrase(articles, nouns, verbs, prepositions)

def nounPhrase(articles, nouns):
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase(articles, nouns, verbs, prepositions):
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase(articles, nouns) + " " + \
           prepositionalPhrase(articles, nouns, prepositions)

def prepositionalPhrase(articles, nouns, prepositions):
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase(articles, nouns)

def main():
    """Allows the user to input the number of sentences
    to generate."""
    articles = getWords("articles.txt")
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    prepositions = getWords("prepositions.txt")

    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence(articles, nouns, verbs, prepositions))

# The entry point for program execution
if __name__ == "__main__":
    main()

