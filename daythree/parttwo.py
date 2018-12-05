#Day 3: No Matter How You Slice It, Part II

#After all the claims have been made in part I, which claim is the only one that does not overlap any other?

import numpy as np
import re

#Open the file. This file comes from https://adventofcode.com/2018/day/3/input. Inputs differ per user.
claims_file = open('input.txt')

#Read each line of the file and save to a variable.
claims = claims_file.readlines()

#Create a 1000x1000 piece of fabric.
fabric = np.zeros((1000, 1000))

whole_claim = ''

def read_claim(claim):
    id = re.search(r"#\d+", claim).group().strip('#')

    position = re.search(r"\d+,\d+", claim).group()
    position = position.split(',')
    left_position = int(position[0])
    top_position = int(position[1])

    size = re.search(r"\d+x\d+", claim).group()
    size = size.split('x')
    width = int(size[0])
    height = int(size[1])

    return id, left_position, top_position, width, height

#Loop through the claims.
for c in claims:
    #Get the id, position and size for the claim.
    id, left_position, top_position, width, height = read_claim(c)

    #Plot the claim on the fabric.
    for i in range(left_position, left_position+width):
        for j in range(top_position, top_position+height):
            if fabric[i][j] == 0:
                fabric[i][j] = id
            #If there is already a claim, mark the square as shared.
            else:
                fabric[i][j] = -1

for c in claims:
    #Initialize overlap to false.
    overlap = False
    
    #Get the id, position and size for the claim.
    id, left_position, top_position, width, height = read_claim(c)

    #Loop through the claim. Check if any squares are marked as overlap.
    for i in range(left_position, left_position+width):
        for j in range(top_position, top_position+height):
            if fabric[i][j] == -1:
                overlap = True
            
    if not overlap:
        whole_claim = id

print(whole_claim)