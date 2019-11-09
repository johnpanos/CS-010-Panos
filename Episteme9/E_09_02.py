"""
 @author John Panos, Christopher French (Westmont College)
 @contact jpanos@westmont.edu, cfrench@westmont.edu
 Created on Thur Oct 7 2019 12:05:05 PM
"""

# Class definition
class ComboLock:
  # Constructor initializes default values
  def __init__(self, secret1, secret2, secret3):
    self.reset()
    self._secret = [secret1, secret2, secret3]

  # On reset, set current position to 0, and history to an empty list of three zeroes
  def reset(self):
    self.currentPos = 0
    self._history = [0] * 3

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
    return self._secret == self._history

  # Private function to simplify adding to the history
  # This function shifts all values to the left, and adds the next value
  def _addHistory(self, toAdd):
    if len(self._history) >= 3:
      self._history.pop(0)
    self._history.append(toAdd)

  # Debug function that prints class state
  # def debug(self):
  #   print("="*10)
  #   print("currentPos: " + str(self.currentPos))
  #   for i in range(0, len(self._history)):
  #     print(str(i) + ": " + str(self._history[i]))
  #   print("="*10)