class Person:
  # Init default instance variables and set them
  def __init__(self, name="", yearOfBirth=1970):
    self.setName(name)
    self.setBirthYear(yearOfBirth)

  # Name Getter
  def getName(self):
    return self._name

  # Name Setter, will validate beforehand
  def setName(self, name):
    self._validateString(name)
    self._name = name

  # Name Getter
  def getBirthYear(self):
    return self._yearOfBirth

  # Birth Year Setter, will validate beforehand
  def setBirthYear(self, yearOfBirth):
    self._validateBirthYear(yearOfBirth)
    self._yearOfBirth = yearOfBirth

  # Will throw exception if string is not an instance of str
  def _validateString(self, string):
    if not isinstance(string, str):
      raise ValueError

  # Will throw exception if integer is not an instance of int
  def _validateInteger(self, integer):
    try:
      int(integer)
    except:
      raise ValueError

  # Will throw exception if year of birth does not meat conditions
  def _validateBirthYear(self, yearOfBirth):
    self._validateInteger(yearOfBirth)
    if yearOfBirth < 1900:
      raise ValueError("Year of birth cannot be below 1900")
    if yearOfBirth > 2016:
      raise ValueError("Year of birth cannot be above 2016")
    return yearOfBirth

  # Representation function
  def __repr__(self):
    return "Name: {0}, Year of Birth: {1}".format(self._name, self._yearOfBirth)


class Student(Person):
  # Init default instance variables and set them
  def __init__(self, name="", yearOfBirth=1970, major="Computer Science"):
    super().__init__(name, yearOfBirth)
    self.setMajor(major)

  # Major Getter
  def getMajor(self):
    return self._major

  # Major Setter, will validate beforehand
  def setMajor(self, major):
    self._validateString(major)
    self._major = major

  # Representation function
  def __repr__(self):
    return "{0}, Major: {1}".format(super().__repr__(), self.getMajor())

class Professor(Person):
  # Init default instance variables and set them
  def __init__(self, name="", yearOfBirth=1970, salary=0):
    super().__init__(name, yearOfBirth)
    self.setSalary(salary)

  # Salary Getter
  def getSalary(self):
    return self._salary

  # Salary setter, will validate beforehand
  def setSalary(self, salary):
    self._validateInteger(salary)
    self._salary = salary

  # Representation function
  def __repr__(self):
    return "{0}, Salary: {1}".format(super().__repr__(), self.getSalary())