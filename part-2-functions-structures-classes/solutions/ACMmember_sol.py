# TODO: Fill out an ACMmember class with any desired functionality
class ACMmember():

  # Define constructor here
  def __init__(self, likesToCode, memberPoints, name, clout, ssn, bobasConsumed):
    self.likesToCode = likesToCode
    self.memberPoints = memberPoints
    self.name = name
    self.clout = clout
    self.ssn = ssn
    self.bobasConsumed = bobasConsumed
  
  # Define some methods (functions) here
  def walkToSixth(self):
    self.clout += 500
  
  def getBoba(self, amount_boba):
    self.bobasConsumed += amount_boba
  
  def hostWorkshop(self):
    self.clout += 1000
    self.bobasConsumed += 5
    self.memberPoints += 10
  
  def deleteSSN(self):
    self.ssn = 5
  
  def goToKickoff(self):
    self.likesToCode = True
    self.memberPoints += 50
    self.bobasConsumed += 2
  

  