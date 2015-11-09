# Anagram Assignment
# Joshua Schoonmaker
# CIS_125

import string


def sortString(word):
    
    # convert word to list
    word = word.lower()
    listWord = list(word)
    
    # sort list
    listWord.sort()
    
    # join list back into sorted word
    sortedLetters = "".join(listWord)
    
    # return sorted word
    return sortedLetters
    

def createDictionary(fileName, dictionary):
    
    # open File
    fileHandle = open(fileName, "r")
    
    # Process line into a word
    for line in fileHandle:
        line = line.strip()
        word = line.lower()
        if word [0] == "v":
            sortedWord = sortString(word)
            dictionary[sortedWord] = word
    fileHandle.close()
    

def findAnagrams(fileName, dictionary):
    fileHandle = open(fileName, "r")
    for line in fileHandle:
        line = line.strip()
        line = line.strip(string.punctuation)
        quizword = line.lower()
        print(quizword, dictionary[sortString(quizword)])
    fileHandle.close()
    
    
def main():
    aDict = {}
    filename = 'wordList.txt'
    quizListName = "quizwords.txt"
    createDictionary(filename, aDict)
    findAnagrams(quizListName, aDict)
    
main()