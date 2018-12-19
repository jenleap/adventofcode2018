#Day 5: Alchemical Reduction, Part II
#For each unit type (both upper and lower), remove from polymer, then complete all reactions. Determine which unit type, when removed, results in the shortest polymer.

#Open the file. This file comes from https://adventofcode.com/2018/day/5/input. Inputs differ per user.
polymer_file = open('input.txt')

#Read the file into a variable.
polymer_list = polymer_file.readlines()

polymer_const = polymer_list[0]

#Get all unit types from the polymer.
unit_types = set(polymer_const.lower())

#Create an empty dictionary to store unit types and polymer lengths.
global unit_dict
unit_dict = dict()

def loop_through():
    global polymer
    global reactions_complete
    i = 0

    #To track whether any reactions are occurred during the loop.
    no_reactions = True

    #Loop through the polymer until we reach the end.
    while (i < len(polymer)-1):
        #If the two chars are equal, no reaction occurs.
        if (polymer[i] == polymer[i + 1]):
            i = i + 1
        #If the two chars are the same but one is lower and the other is upper, a reaction occurs and both chars are removed.
        elif (polymer[i].lower() == polymer[i + 1].lower()):
            no_reactions = False
            if (i >= len(polymer)):
                polymer = polymer[:i]
            else:
                polymer = polymer[:i] + polymer[i+2:]
        #If the two chars are different, no reaction occurs.
        else:
            i = i + 1
    
    #Once the loop has been completed, check if any reactions have occurred. If none have occurred, set the polymer as complete.
    if (no_reactions):
        reactions_complete = True

#Loop through all unit types.
for unit in unit_types:
    #All reactions are not finished
    reactions_complete = False

    #Remove both upper and lower case of that unit type from polymer. 
    polymer = polymer_const.replace(unit, "")
    polymer = polymer.replace(unit.upper(), "")

    #Loop through the polymer until all reactions have been completed.
    while (not reactions_complete):
        loop_through()

    #Enter unit type and polymer length into dictionary.
    unit_dict[unit] = len(polymer)

print(min(unit_dict.values()))

