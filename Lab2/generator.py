import random

def getArticles(articleFile, articles):
    with open(articleFile, "r") as file:
        element = file.read()
        articles.append(element)

def getNouns(nounFile, nouns):
    with open(nounFile, "r") as file:
        element = file.read()
        nouns.append(element)

def getVerbs(verbFile, verbs):
    with open(verbFile, "r") as file:
        element = file.read()
        verbs.append(element)

def getPrepositions(prepositionFile, prepositions):
    with open(prepositionFile, "r") as file:
        element = file.read()
        prepositions.append(element)
        
def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()
    
articles = []
nouns = []
verbs = [] 
prepositions = []

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()

