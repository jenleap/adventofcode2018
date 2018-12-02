#Day 1: Chronal Calibration
#Given a file containing frequency inputs, calculate the resulting frequency after all the changes in frequency have been applied.

#Open the file. This file comes from https://adventofcode.com/2018/day/1/input. Inputs differ per user.
frequency_inputs = open('input.txt')

#Read each line of the file and save to a variable.
frequencies_raw = frequency_inputs.readlines()

#Initialize the total variable to zero.
frequency_total = 0

#Loop through the list of frequencies. For each frequency, remove the new line char and convert to an integer. Add the resulting integer to the total.
for f in frequencies_raw:
    cleaned = int(f.strip('\n'))
    frequency_total += cleaned

#Return the total
print(frequency_total)