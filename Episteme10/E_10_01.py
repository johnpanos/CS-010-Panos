class Person:
  def __init__(self, name, yearOfBirth):
    self._name = name
    self._yearOfBirth = yearOfBirth

class Student(Person):
  def __init__(self, name, yearOfBirth, major):
    super().__init__(name, yearOfBirth)
    self._major = major

class Professor(Person):
  def __init__(self, name, yearOfBirth, salary):
    super().__init__(name, yearOfBirth)
    self._salary = salary