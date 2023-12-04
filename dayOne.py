def return_first_integer(line):
    for character in line:
        if character.isdigit():
           return character

def return_last_integer(line):
    for character in reversed(line): # Iterates starting from the back
        if character.isdigit():
           return character

def return_calibration_value_of_row(line):
    return return_first_integer(line) + return_last_integer(line) # Returns a string

def get_number_from_file(file_path):
    "Goes through the file, line by line, and adds the number to a total. Return the total."
    total_number = 0
    with open(file_path, 'r') as file:
        for line in file:
            #print(int(return_calibration_value_of_row(line.strip())))
            total_number += int(return_calibration_value_of_row(line.strip()))
    return total_number


print(get_number_from_file('day1input.txt'))
print(get_number_from_file('day1input2modified.txt'))
#print(get_number_from_file('dayonetest.txt'))


# Part 1 replaces
# one -> o1e
# two -> t2o
# three -> t3e
# Four -> f4r
# Five -> f5e
# Six -> s6x
# Seven -> s7n
# Eight -> e8t
# Nine -> n9e
