def wordCounter(filename, wordList):
  countList = [0] * len(wordList)
  try:
    myFile = open(filename, "r")
    for line in myFile:
      lineList = line.split(" ")
      for word in lineList:
        strippedWord = word.strip().strip(".").strip(",").strip("!").strip("?").lower()
        for i in range(0, len(wordList)):
          if strippedWord == wordList[i].lower():
            countList[i] += 1
  except IOError:
    print("Could not open the file:", filename)
  for i in range(0, len(wordList)):
      word = wordList[i].lower()
      wordCount = countList[i]
      print('{:^23}'.format(word + " : " + str(wordCount)))


filename = "FrozenScript.txt"
print("*****")
print(filename)
wordCounter(filename, ["he", "she", "it", "Olaf", "Anna"])
print("*****")
filename = "dummy.txt"
print(filename)
wordCounter(filename, ["he", "she", "it"])
print("*****")