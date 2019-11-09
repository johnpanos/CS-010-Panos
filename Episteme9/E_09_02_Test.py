from E_09_02 import ComboLock

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