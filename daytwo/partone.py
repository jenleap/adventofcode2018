#Day 2: Inventory Management
#Check box labels and count chars appearing exactly twice and exactly three times. Multiply these together to produce a checksum result.

#Open the file. This file comes from https://adventofcode.com/2018/day/2/input. Inputs differ per user.
label_file = open('input.txt')

#Read each line of the file and save to a variable.
box_labels = label_file.readlines()

#Initialize the total variables to zero.
double_count = 0
triple_count = 0

#Loop through the list of labels. Loop through the chars in each string. Check for double or triple counts. Remove the chars from string after it has been counted.
for l in box_labels:
    double_already = False
    triple_already = False
    for char in l:   
        if ((l.count(char) == 2) and not double_already):
            double_count += 1
            double_already = True
        if ((l.count(char) == 3) and not triple_already):
            triple_count += 1
            triple_already = True
        l = l.replace(char, '')

#Return the checksum.
print(double_count * triple_count)