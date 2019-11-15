class Person:
  def __init__(self, name="", yearOfBirth=1970):
    self.setName(name)
    self.setBirthYear(yearOfBirth)

  def getName(self):
    return self._name

  def setName(self, name):
    self._validateString(name)
    self._name = name

  def getBirthYear(self):
    return self._yearOfBirth

  def setBirthYear(self, yearOfBirth):
    self._validateBirthYear(yearOfBirth)
    self._yearOfBirth = yearOfBirth

  

  def _validateString(self, string):
    if not isinstance(string, str):
      raise ValueError

  def _validateInteger(self, integer):
    try:
      int(integer)
    except:
      raise ValueError

  def _validateBirthYear(self, yearOfBirth):
    self._validateInteger(yearOfBirth)
    if yearOfBirth < 1900:
      raise ValueError("Year of birth cannot be below 1900")
    if yearOfBirth > 2016:
      raise ValueError("Year of birth cannot be above 2016")
    return yearOfBirth

  def __repr__(self):
    return "Name: {0}, Year of Birth: {1}".format(self._name, self._yearOfBirth)


class Student(Person):
  def __init__(self, name="", yearOfBirth=1970, major="Computer Science"):
    super().__init__(name, yearOfBirth)
    self.setMajor(major)

  def getMajor(self):
    return self._major

  def setMajor(self, major):
    self._validateString(major)
    self._major = major

  def __repr__(self):
    return "{0}, Major: {1}".format(super().__repr__(), self.getMajor())

class Professor(Person):
  def __init__(self, name="", yearOfBirth=1970, salary=0):
    super().__init__(name, yearOfBirth)
    self.setSalary(salary)

  def getSalary(self):
    return self._salary

  def setSalary(self, salary):
    self._validateInteger(salary)
    self._salary = salary

  def __repr__(self):
    return "{0}, Salary: {1}".format(super().__repr__(), self.getSalary())