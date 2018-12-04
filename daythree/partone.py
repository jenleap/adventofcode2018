#Day 3: No Matter How You Slice It

#Given a square of fabric and claims made to areas of the fabric, calculate how many square inches of fabric are within two or more claims. 
#For #123 @ 3,2: 5x4, ID is 123, 3 in from left edge, 2 in from top edge, 5 in wide and 4 in tall.

import numpy as np
import re

#Open the file. This file comes from https://adventofcode.com/2018/day/3/input. Inputs differ per user.
claims_file = open('input.txt')

#Read each line of the file and save to a variable.
claims = claims_file.readlines()

#Create a 1000x1000 piece of fabric.
fabric = np.zeros((1000, 1000))

#Loop through the claims.
for c in claims:
    #Get the id, position and size for the claim.
    id = re.search(r"#\d+", c).group().strip('#')

    position = re.search(r"\d+,\d+", c).group()
    position = position.split(',')
    left_position = int(position[0])
    top_position = int(position[1])

    size = re.search(r"\d+x\d+", c).group()
    size = size.split('x')
    width = int(size[0])
    height = int(size[1])

    #Plot the claim on the fabric.
    for i in range(left_position, left_position+width):
        for j in range(top_position, top_position+height):
            if fabric[i][j] == 0:
                fabric[i][j] = id
            #If there is already a claim, mark the square as shared.
            else:
                fabric[i][j] = -1

#Sum up all the shared squares of fabric.
shared_squares = (fabric == -1).sum()

print(shared_squares)

