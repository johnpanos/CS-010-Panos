from E_10_01 import Person

#Test default constructor, and getters
djp3 = Person()
if(djp3.getName() != ""):
    raise Exception("Test failed: default name was not blank")
if(djp3.getBirthYear() != 1970):
    raise Exception("Test failed: default birthyear was not 1970")

#Test setters
testName = "Prof. Patterson"
testYear = 1972
djp3 = Person()
djp3.setName(testName)
if(djp3.getName() != testName):
    raise Exception("Test failed: setName did not work")
djp3.setBirthYear(testYear)
if(djp3.getBirthYear() != testYear):
    raise Exception("Test failed: setBirthYear did not work")

#Test correct call of constructor
testName = "Prof. Patterson"
testYear = 1972
djp3 = Person(testName,testYear)
if(djp3.getName() != testName):
    raise Exception("Test failed: constructor didn't set name")
if(djp3.getBirthYear() != testYear):
    raise Exception("Test failed: constructor didn't set birth year")

#Test bad types in constructor parameters
try:
    testName = 1972
    testYear = 1972
    djp3 = Person(testName,testYear)
    raise Exception("Test failed: constructor allows an integer for a name")
except ValueError:
    pass

#Test bad types in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = "Prof. Patterson"
    djp3 = Person(testName,testYear)
    raise Exception("Test failed: constructor allows a string for a birth year, should be restricted to an int")
except ValueError:
    pass

#Test bad values in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = 1899
    djp3 = Person(testName,testYear)
    raise Exception("Test failed: Allowed a date too far in the past")
except ValueError:
    pass

#Test bad values in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = 2017
    djp3 = Person(testName,testYear)
    raise Exception("Test failed: Allowed a year too far in the future ")
except ValueError:
    pass

#Test bad values in setters parameters
try:
    djp3 = Person()
    testYear = 1899
    djp3.setBirthYear(testYear)
    raise Exception("Test failed: Allowed a date too far in the past")
except ValueError:
    pass

#Test bad values in setters parameters
try:
    djp3 = Person()
    testYear = 2017
    djp3.setBirthYear(testYear)
    raise Exception("Test failed: Allowed a year too far in the future ")
except ValueError:
    pass

#Test string representation
testName = "Prof. Iba"
testYear = 1965
djp3 = Person(testName,testYear)
if(str(djp3) != "Name: "+testName+", Year of Birth: "+str(testYear)):
    raise Exception("Test failed with wrong string representation: "+str(djp3))

print("Person class passed all tests")
