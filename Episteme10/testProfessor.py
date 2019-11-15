from E_10_01 import Professor

#Test default constructor, and getters
djp3 = Professor()
if(djp3.getName() != ""):
    raise Exception("Test failed: default name was not blank")
if(djp3.getBirthYear() != 1970):
    raise Exception("Test failed: default birthyear was not 1970")
if(djp3.getSalary() != 0):
    raise Exception("Test failed: default salary was not 0")

#Test setters
testName = "Prof. Patterson"
testYear = 1972
testSalary = 80000
djp3 = Professor()
djp3.setName(testName)
if(djp3.getName() != testName):
    raise Exception("Test failed: setName did not work")
djp3.setBirthYear(testYear)
if(djp3.getBirthYear() != testYear):
    raise Exception("Test failed: setBirthYear did not work")
djp3.setSalary(testSalary)
if(djp3.getSalary() != testSalary):
    raise Exception("Test failed: setSalary did not work")

#Test correct call of constructor
testName = "Prof. Patterson"
testYear = 1972
testSalary = 80000
djp3 = Professor(testName,testYear,testSalary)
if(djp3.getName() != testName):
    raise Exception("Test failed: constructor didn't set name")
if(djp3.getBirthYear() != testYear):
    raise Exception("Test failed: constructor didn't set birth year")
if(djp3.getSalary() != testSalary):
    raise Exception("Test failed: setSalary did not work")

#Test bad types in constructor parameters
try:
    testName = 1972
    testYear = 1972
    testSalary = 1972
    djp3 = Professor(testName,testYear,testSalary)
    raise Exception("Test failed: constructor allows an integer for a name")
except ValueError:
    pass

#Test bad types in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = "Prof. Patterson"
    testSalary = "Prof. Patterson"
    djp3 = Professor(testName,testYear,testSalary)
    raise Exception("Test failed: constructor allows a string for a birth year, should be restricted to an int")
except ValueError:
    pass

#Test bad types in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = 1972
    testSalary = "250 gallons of wine, annually"
    djp3 = Professor(testName,testYear,testSalary)
    raise Exception("Test failed: constructor allows an string for a salary, should be restricted to an int")
except ValueError:
    pass

#Test bad values in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = 1899
    testSalary = 80000
    djp3 = Professor(testName,testYear,testSalary)
    raise Exception("Test failed: Allowed a date too far in the past")
except ValueError:
    pass

#Test bad values in constructor parameters
try:
    testName = "Prof. Patterson"
    testYear = 2017
    testSalary = 80000
    djp3 = Professor(testName,testYear,testSalary)
    raise Exception("Test failed: Allowed a year too far in the future ")
except ValueError:
    pass

#Test bad values in setters parameters
try:
    djp3 = Professor()
    testYear = 1899
    djp3.setBirthYear(testYear)
    raise Exception("Test failed: Allowed a date too far in the past")
except ValueError:
    pass

#Test bad values in setters parameters
try:
    djp3 = Professor()
    testYear = 2017
    djp3.setBirthYear(testYear)
    raise Exception("Test failed: Allowed a year too far in the future ")
except ValueError:
    pass

#Test string representation
testName = "Prof. Iba"
testYear = 1965
testSalary = 80000
djp3 = Professor(testName,testYear,testSalary)
if(str(djp3) != "Name: "+testName+", Year of Birth: "+str(testYear)+", Salary: "+str(testSalary)):
    raise Exception("Test failed with wrong string representation: "+str(djp3))

print("Professor class passed all tests")
