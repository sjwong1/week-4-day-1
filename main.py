# Problem Set: Working with Numbers & Strings in Python

#################### PROBLEM 1: Types of Numbers & Basic Arithmetic ####################
# Task 1: Declare an integer named 'age' with a value of 25.
# Print out its type to ensure it's an integer.
age1 = 25 
print (age1)
# Task 2: Declare a float named 'height' with a value of 5.9 (which represents someone's height in feet).
# Print out its type to ensure it's a float.

height1 = 5.9

print(height1)
print(type(height1))

# Task 3: What is the data type of the result when 'age' is divided by 'height'? 
# Write the code to find out.

divided = age1 / height1
print(type(divided))

#################### PROBLEM 2: Data Type Conversions ####################
# Task 4: Convert the 'age' to float and 'height' to integer.
# Print out both converted values.

age = float(age1)
height = int(height1)

print(age)
print(height)

# Task 5: Add the original 'age' and 'height' values.
# Convert the result into an integer and then print it.

total = age1 + height1

print (total)
#################### PROBLEM 3: Formatting Strings ####################
# Task 6: You are given the following variables:
team_name = "Los Angeles Lakers"
championships_won = 17

print(f" The {team_name} have won {championships_won} championships! ")
# Use string formatting to print: "The Los Angeles Lakers have won 17 championships!"

# Task 7: Create two new variables:
points_game1 = 89
points_game2 = 102

total_points = points_game1 + points_game2

point_difference = points_game2 - points_game1 

print (f" The total points are {total_points}.")
print (f" the difference in points is {point_difference}")
# Use string formatting to print: "The team scored 89 points in game 1 and 102 points in game 2."

print (f"The team scored {points_game1} in game 1 and {points_game2} in game 2.") 
# Task 8: Calculate the average points across both games and print:
# "The average points over two games is: [average_points]!"
# Ensure average_points is a float with one decimal.
average_points = total_points / 2

print (f"In average they scored {average_points} per game.")
#################### END OF PROBLEM SET ####################


