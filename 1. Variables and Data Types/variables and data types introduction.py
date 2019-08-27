# First program ever
print("Hello Python")

""" 
    Code without comments is useless 
    to everybody else 
    and to yourself 
"""

""" 
Variables

"""
# Temporary storage of a value in a computer program

m = 1 # Gradient
x = 2 # x-axes values
c = 0 # Intercept
y = m * x + c # Straight Line formula
print(y) # Display value of y given the above values

dozen = 12 # Tell the computer that a dozen = 12
half_dozen = 6 # Tell the computer that a half dozen = 6
print("Dozen = ", dozen, sep=" ")
print("Dozen = ", dozen, sep=" ")

""" Literals """
print('219000')


""" 
Data Types 

"""

# Boolean
true_false = True # Only 2 possible values True or False

# Integers
whole_number = 1 # Integer values

# Double
decimal_value = 0.99999 # Decimal Values

# Strings
text_value = 'Howzit' # Single or double quotes can be used for strings

# Lists / Arrays
prime_numbers = [1,2,3,5,7] # Ordered list of integers representing prime numbers

# Tuple
first_quarter_month_names = ('January','February','March')

# Dictionary
first_quarter_sales = [{'January':5000,'February':3000,'March':4000}] # Very special double feature list

# Set
prime_numbers_set = {1,2,3,5,7} # Unordered list of integers representing prime numbers


""" 
Basic Functions 

"""

type(first_quarter_month_names) # Type function used to determine the data type of a variable

print("Hello World") # Print function prints values to the console as output

float(whole_number) # Change/cast a whole number to decimal 1 == 1.0

help() # Opens the built in help function in the python console

""" 
    Use the python help function for additional casting functions:
    float()
    int()
    str()
    etc.. 
"""



