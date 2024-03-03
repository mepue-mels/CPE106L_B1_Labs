import random

def getArticles(articleFile):
    tempList = []
    with open(articleFile, "r") as file:
        tempList.extend(line.strip() for line in file)
    return tuple(tempList)

def getNouns(nounFile):
    tempList = []
    with open(nounFile, "r") as file:
        tempList.extend(line.strip() for line in file)
    return tuple(tempList)

def getVerbs(verbFile):
    tempList = []
    with open(verbFile, "r") as file:
        tempList.extend(line.strip() for line in file)
    return tuple(tempList)

def getPrepositions(prepositionFile):
    tempList = []
    with open(prepositionFile, "r") as file:
        tempList.extend(line.strip() for line in file)
    return tuple(tempList)

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

articleFile = "articles.txt"
nounFile = "nouns.txt"
verbFile = "verbs.txt"
prepositionFile = "prepositions.txt"

articles = getArticles(articleFile)
nouns = getNouns(nounFile)
verbs = getVerbs(verbFile)
prepositions = getPrepositions(prepositionFile)


def main():
    """Allows the user to input the number of sentences
    to generate."""

    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()

