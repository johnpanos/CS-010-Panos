def parseFile(file):
  # Open file with filename
  fileHandle = open(file, "r")
  # For every country, parse the data and put it in a dictionary
  # with the key being the country, and the value being the number
  # either the gini number or life expectancy
  fileDict = dict()
  for line in fileHandle:
    lineList = line.split(":")
    fileDict[lineList[1].strip(" ")] = float(lineList[2])
  return fileDict  

def main():
  # Load files into memory using dictionary (key value)
  lifeDict = parseFile("life.txt")
  giniDict = parseFile("gini.txt")

  # Add all countries to a set so we get rid of duplicates
  cSet = set()
  for country in lifeDict:
    cSet.add(country)
  for country in giniDict:
    cSet.add(country)

  # Sort the list in alphabetical order
  cList = sorted(list(cSet))

  cInput = ""
  while cInput != "q":
    cInput = input("Please enter a country (q to quit): ")

    # Don't run country lookup for q
    if cInput == "q":
      continue

    # If country input is in dictionaries print available data
    if cInput in lifeDict:
      print("  Life Expectancy is %.1f years at birth" % lifeDict[cInput])
    else:
      print("  No Life Expectancy Data")
    if cInput in giniDict:
      print("  Gini Value is %.1f" % giniDict[cInput])
    else:
      print("  No Gini Data")

    # If in neither, print suggestions
    if cInput not in lifeDict and cInput not in giniDict:
      print("  Maybe you meant:")
      newWord = cInput.lower()
      for country in cList:
        if country.lower()[0] == newWord[0] and country != None:
          print("   " + country)
    
# Get the ball rollin'
main()