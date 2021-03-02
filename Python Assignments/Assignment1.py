# Ryan Castles, 6433236, CSIT110

# Question 1

print("Question 1. \n")

#Get input from user for title and author.
song_title = input("Your favourite song title: ")
song_author = input("Your favourite song author: ")

print()

#print the string using string addition.
print("Using string addition")
print("Your favourite song is " + song_title + " by " + song_author + ".")

print()

# Question 2

print("Question 2. \n")

#Get input from user for 3 integers and convert to int.
first_integer = input("Please enter the 1st positive integer: ")
number1 = int(first_integer)
second_integer = input("Please enter the 2nd positive integer: ")
number2 = int(second_integer)
third_integer = input("Please enter the 3rd positive integer: ")
number3 = int(third_integer)

#Calculate the result
result = number1 * number2 * number3

print()
print("Display using string addition: ")
print("Equation: " + str(first_integer) + " x " + str(second_integer) + " x " + str(third_integer) + " = " + str(result))

print()

# Question 3

print("Question 3. \n")

#Get input from user for the first subject and convert credit to int.
first_code = input("Enter the 1st subject code: ")
first_title = input("Enter the 1st subject title: ")
first_credit_point = input("Enter the 1st subject credit point: ")
credit_value1 = int(first_credit_point)

print()

#Get input from user for the second subject and convert credit to int.
second_code = input("Enter the 2nd subject code: ")
second_title = input("Enter the 2nd subject title: ")
second_credit_point = input("Enter the 2nd subject credit point: ")
credit_value2 = int(second_credit_point)

print()

#Display chosen subjects.
print("Your chosen subjects:") 
print(first_code + ": " + first_title)
print(second_code + ": " + second_title)
print("Total credit points: " + str(credit_value1 + credit_value2)) 

print()

# Question 4

print("Question 4. \n")

#Get input from user an convert to integer value.
one_hundred_level = input("How many 100-level subjects you have completed: ")
one_hundred_credit = int(one_hundred_level) * 4

two_hundred_level = input("How many 200-level subjects you have completed: ")
two_hundred_credit = int(two_hundred_level) * 5

three_hundred_level = input("How many 300-level subjects you have completed: ")
three_hundred_credit = int(three_hundred_level) * 6

#Calculations
subject_count = int(one_hundred_level) + int(two_hundred_level) + int(three_hundred_level)
total_credit = one_hundred_credit + two_hundred_credit + three_hundred_credit

print()

#print using formatting
print("{0:<8}{1:<13}{2:>10}".format("Level", "Subject Count", "Credit"))
print("{0:<8}{1:>13}{2:>10}".format("100", str(one_hundred_level), str(one_hundred_credit)))
print("{0:<8}{1:>13}{2:>10}".format("200", str(two_hundred_level), str(two_hundred_credit)))
print("{0:<8}{1:>13}{2:>10}".format("300", str(three_hundred_level), str(three_hundred_credit)))
print("{0:<8}{1:>13}{2:>10}".format("Total", str(subject_count), str(total_credit)))

print()

# Question 5

print("Question 5. \n")

#Grab user input for adult tickets and convert to int then format.
adult_tickets = input("How many adult tickets you want to order: ")
adult_cost = int(adult_tickets) * 50.5
formatted_adult_cost = "{:.2f}".format(adult_cost)

#User input for child over 10
child_over_ten = input("How many children (>=10 years old) tickets: ")
child_over_cost = int(child_over_ten) * 10.5
formatted_child_over = "{:.2f}".format(child_over_cost)

#User input for child under 10
child_under_ten = input("How many children (<10 years old) tickets: ")
child_under_cost = "free"

total_cost = "{:.2f}".format(adult_cost + child_over_cost)

#Calculate total tickets
total_tickets = int(adult_tickets) + int(child_over_ten) + int(child_under_ten)

print()

#Print using formatting.
print("{0:<18}{1:>17}{2:>15}".format("Type", "Number of tickets", "Cost"))
print("{0:<18}{1:>17}{2:>15}".format("Adult", str(adult_tickets), "$" + str(formatted_adult_cost)))
print("{0:<18}{1:>17}{2:>15}".format("Children (>=10)", str(child_over_ten),"$" + str(formatted_child_over)))
print("{0:<18}{1:>17}{2:>15}".format("Children (<10)", str(child_under_ten), child_under_cost))
print("{0:<18}{1:>17}{2:>15}".format("Total", str(total_tickets), "$" + str(total_cost)))
