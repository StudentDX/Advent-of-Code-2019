import csv
import sys
sys.path.append('..\day1')
from day1 import findFuelRequirement

def findFuelRequirementRec(mass):
    FR = findFuelRequirement(mass)
    #print (FR)
    if (FR > 0):
        return FR + findFuelRequirementRec(FR)
    else:
        return 0
    
#print (findFuelRequirementRec(14))
#print (findFuelRequirementRec(1969))
#findFuelRequirementRec(1969)

def findFuelRequirementRecSum(route):
    output = 0
    with open(route) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            mass = (int)(row[0])
            output += findFuelRequirementRec(mass)
    return output
    
print (findFuelRequirementRecSum("input.csv"))