"""
 @author John Panos, Marcus Kurschat (Westmont College)
 @contact jpanos@westmont.edu, mkurschat@westmont.edu
 Created on Mon Oct 20 2019 11:52:37 AM
"""

def wordFilter(filename):
  # Init variables to use for results
  wordList = []
  countList = []
  totalCount = 0

  # Open the file and let the user know if it fails
  try:
    myFile = open(filename, "r")
    # Iterate over the whole script and every word, and count every time it's used
    for line in myFile:
      lineList = line.split(" ")
      for word in lineList:
        totalCount += 1
        strippedWord = word.strip().strip(".").strip(",").strip("!").strip("?").strip("(").strip(")").strip("-").lower()
        if len(strippedWord) > 1:
          if strippedWord not in wordList:
            wordList.append(strippedWord)
            countList.append(1)
          else:
            countList[wordList.index(strippedWord)] += 1
    # Iterate over the results and print to screen if the word's count is over 1% of the total word count
    for i in range(0, len(wordList)):
      if countList[i] > totalCount * 0.01:
        print('{:>10}{:}{:<5}'.format(wordList[i], " : ", str(countList[i])))
  except IOError:
    print("Could not open the file:", filename)