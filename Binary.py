# Compulsory Task 1

# You could just use this method
binary_num = input('Please enter a binary number that you would like to convert to decimal: ')
print('The number you entered is: ' + str(int(binary_num, 2)))

# Or you could use this
# Import the math module
import math

# Ask the user to enter a binary number and split it into a list of 1s and 0s
binary_num = input('Please enter a binary number that you would like to convert to decimal: ')
binary_num_space = binary_num.replace(''," ")
binary_num_split = binary_num_space.split()
int_binary_num_split = [int(num) for num in binary_num_split]

# This is the length of the list -1 to get the exponents used in the decimal calculation
exp = len(int_binary_num_split) - 1

# Empty decimal value
decimal = 0

# This loop will run for every character (single number) in the binary code
for num in int_binary_num_split:
    power = num * (2**exp)
    decimal += power
    exp -= 1 # This will decrease down to 0

print('The number you entered is: ' + str(decimal)) # Prints out the final value





