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
    # Clamp the values of the secret from range 0-39 to match the lock
    self._secret = [self._clamp(secret1), self._clamp(secret2), self._clamp(secret3)]

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

  # Clamp the number between the range of 0-39
  def _clamp(self, number):
    if number > 39:
      return 39
    if number < 0:
      return 0
    return number

  # Private function to simplify adding to the history
  # This function shifts all values to the left, and adds the next value
  def _addHistory(self, toAdd):
    if len(self._history) >= 3:
      self._history.pop(0)
    self._history.append(toAdd)