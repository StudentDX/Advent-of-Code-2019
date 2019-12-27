import csv

def findFuelRequirement(mass):
    output = (int)(mass / 3) - 2
    return output
    
def findFuelRequirementSum():
    output = 0
    with open("input.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            mass = (int)(row[0])
            #print ((int)(row[0]))
            output += findFuelRequirement(mass)
            #print (output)
    print (output)
        
findFuelRequirementSum()
