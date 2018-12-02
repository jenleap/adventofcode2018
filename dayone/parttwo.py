#Day 1: Chronal Calibration, Part II
#The previous file tracks the resulting total from input frequencies. Calculate when the frequency total has reached a duplicate frequency.

#Open the file. This file comes from https://adventofcode.com/2018/day/1/input. Inputs differ per user.
frequency_inputs = open('input.txt')

#Initialize the total variable to zero and the list of frequencies to an empty array.
frequency_total = 0
total_list = []

#Check to see if the frequency total has already been reached. If not, add the frequency to the list and read the next frequency.
while frequency_total not in total_list:
    total_list.append(frequency_total)
    frequency_raw = frequency_inputs.readline()

    #If readline() returns an empty string, end of file has been reached. Return to beginning of file and start again.
    if ("" == frequency_raw):
        frequency_inputs.seek(0)
        frequency_raw = frequency_inputs.readline()

    cleaned = int(frequency_raw.strip('\n'))
    frequency_total += cleaned

#Return the total
print(frequency_total)