"""
 @author John Panos (Westmont College)
 @contact jpanos@westmont.edu
 Created on Fri Oct 25 2019 12:05:05 PM
"""

# Class definition
class ComboLock:
  # Constructor initializes default values
  def __init__(self, secret1, secret2, secret3):
    self.reset()
    self.secret = [secret1, secret2, secret3]

  # On reset, set current position to 0, and history to an empty list of three zeroes
  def reset(self):
    self.currentPos = 0
    self.history = [0] * 3

  # Upon turning left, change the position by adding to the current pos, and get current 
  # pos using currentPos modulo 40 and adding the current pos to the history list
  def turnLeft(self, ticks):
    self.currentPos = (self.currentPos + ticks) % 40
    self._addHistory(self.currentPos)

  # See above comment, but instead of adding, subtract
  def turnRight(self, ticks):
    self.currentPos = (self.currentPos - ticks) % 40
    self._addHistory(self.currentPos)
  
  # Check to see if the value of the secret list equals
  # to the list of the last three currentPos values
  def open(self):
    return self.secret == self.history

  # Private function to simplify adding to the history
  # This function shifts all values to the left, and adds the next value
  def _addHistory(self, toAdd):
    if len(self.history) >= 3:
      self.history.pop(0)
    self.history.append(toAdd)

  # Debug function that prints class state
  # def debug(self):
  #   print("="*10)
  #   print("currentPos: " + str(self.currentPos))
  #   for i in range(0, len(self.history)):
  #     print(str(i) + ": " + str(self.history[i]))
  #   print("="*10)

myLock = ComboLock(10,20,10)
myLock.reset()
myLock.turnRight(30)
myLock.turnLeft(10)
myLock.turnRight(10)
if(myLock.open() == True):
  print("The lock opened") #Correct outcome
else:
  print("The lock didn't open")
myLock.reset()
myLock.turnLeft(30)
myLock.turnRight(10)
myLock.turnLeft(10)
if(myLock.open() == True):
  print("The lock opened")
else:
  print("The lock didn't open") #Correct outcome