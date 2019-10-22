"""
 @author John Panos, Marcus Kurschat (Westmont College)
 @contact jpanos@westmont.edu, mkurschat@westmont.edu
 Created on Mon Oct 20 2019 11:51:37 AM
"""

def wordCounter(filename, wordList):
  # Init list for the count of words
  countList = [0] * len(wordList)
  # Try to open the file and if it fails, tell user
  try:
    # Get file handler for the filename
    myFile = open(filename, "r")
    # For every line, split it into 
    for line in myFile:
      # Split into list so we can iterate over it
      lineList = line.split(" ")
      for word in lineList:
        # Strip the word so we just get the word
        strippedWord = word.strip().strip(".").strip(",").strip("!").strip("?").strip("(").strip(")").strip("-").lower()
        # Count how many times it exists
        for i in range(0, len(wordList)):
          if strippedWord == wordList[i].lower():
            countList[i] += 1
  # Catch the error and let the user know that the file doesn't exist
  except IOError:
    print("Could not open the file:", filename)
  # For every word output the results it to the console
  for i in range(0, len(wordList)):
      word = wordList[i].lower()
      wordCount = countList[i]
      print('{: >10}{:}{: <5}'.format(word, " : ", str(wordCount)))