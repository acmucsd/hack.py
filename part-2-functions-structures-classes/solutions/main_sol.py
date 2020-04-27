# Import and test your ACMmember class here. 
from ACMmember import ACMmember
# Create objects and verify methods serve the proper functionality

bryce = ACMmember(True, 700, "Bryce", 20000, 2, 100)
print(bryce.clout)
bryce.walkToSixth()
print(bryce.clout)

elias = ACMmember(False, 100, "Elias", -1000, 1234567890, 0)
print(elias.bobasConsumed)
elias.hostWorkshop()
print(elias.bobasConsumed)

thomas = ACMmember(True, 1, "Thomas", 4, -70, 20)
print("Thomas's Membership points were " + str(thomas.memberPoints))
thomas.goToKickoff()
thomas.deleteSSN()

print("Thomas's Membership Points are now: " + str(thomas.memberPoints))
print("His SSN is: " + str(thomas.ssn))

# likesToCode, memberPoints, name, clout, ssn, bobasConsumed
