# How do you print something?

# You can print a string.
print("Hello World")
# You can print a number.
print(123.456)

# You can print a boolean value.
print(True)

# How do you set a variable?
first_name = "John Smith"

# You can set a variable to a string, number, and a boolean value.
variable = 0
variable1 = "Hello"
variable2 = True

#-----------------------------------------------------------------------------------------------------------------------

# Conversion of string to int.
# number1 = input("Give me a number: ")
# answer = 19.95 - number1 ----------------------------------------------------------------------------- PROBLEMS ------

# This will not work. number1 is a STR, and needs to be converted to an INT to be subtracted from 19.95.

# CORRECT CODE:
number1 = input("Give me a number: ")
answer = 19.95 - int(number1)  # You have to put int(_____) in front of the number1.
print(number1 + " subtracted from 19.95 is " + str(answer))  # INT conversion back to STR.

#_______________________________________________________________________________________________________________________
# Conversion of INT to STR.
number1 = input("Give me a number: ")
answer = 19.95 - int(number1)  # You have to put int(_____) in front of the number1.
# print(number1 + " subtracted from 19.95 is " + answer)  # INT conversion back to STR.
# You have to put str(____) around ANSWER, in order to be problem-free. ANSWER comes in INT, so you have to make it STR.

# CORRECT CODE:
number1 = input("Give me a number: ")
str_answer = 19.95 - int(number1)  # You have to put int(_____) in front of the number1.
print(number1 + " subtracted from 19.95 is " + str(str_answer))  # INT conversion back to STR.

# You can convert things to FLOATS, INTs, and STRs.


