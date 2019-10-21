'''
 @author John Panos, Marcus Kurschat (Westmont College)
 @contact jpanos@westmont.edu, mkurschat@westmont.edu
 Created on Mon Oct 21 2019 11:52:37 AM
'''

def wordCounter(filename, wordList):
  # Init list for the count of words
  countList = [0] * len(wordList)
  # 
  try:
    # Get file handler for the filename
    myFile = open(filename, "r")
    # For every line, split it into 
    for line in myFile:
      lineList = line.split(" ")
      for word in lineList:
        strippedWord = word.strip().strip(".").strip(",").strip("!").strip("?").lower()
        for i in range(0, len(wordList)):
          if strippedWord == wordList[i].lower():
            countList[i] += 1
  # Catch the error and let the user know that the file doesn't exist
  except IOError:
    print("Could not open the file:", filename)
  # For every word output it to the console
  for i in range(0, len(wordList)):
      word = wordList[i].lower()
      wordCount = countList[i]
      print('{:^23}'.format(word + " : " + str(wordCount)))

def wordFilter(filename):
  try:
    myFile = open(filename, "r")
  except:
    print("Could not open the file:", filename)

filename = "FrozenScript.txt"
print("*****")
print(filename)
# wordCounter(filename, ["he", "she", "it", "Olaf", "Anna"])
wordFilter(filename)
print("*****")
filename = "dummy.txt"
# print(filename)
# wordCounter(filename, ["he", "she", "it"])
# print("*****")