# Ryan Castles, 6433236, CSIT110

import random

# Question 1

print("Question 1")
print()

def fee_calculation(adult_count, child_count): #Function takes two arguments, adult_count and child_count
    adult_total = int(adult_count) * 20 #calc adult_total
    child_total = int(child_count) * 10 #calc child_total
    
    total_cost = adult_total + child_total #calc total cost

    if (total_cost > 100):
        total_cost = total_cost - (0.1 * total_cost) #calc discount

    return "{:.0f}".format(total_cost) #format to no decimal places

#get user input and print cost
adult_count = input("Enter number of adult tickets: ")
child_count = input("Enter number of child tickets: ")
print()
print("The cost is $" + str(fee_calculation(adult_count, child_count)))


# Question 2

print()
print("Question 2")
print()

def display_equations(number_start, number_end): #define function with two arguments
    for i in range(int(number_start), int(number_end) + 1): #for loop to loop through start to end number
        result = i + (i+1) + (i+2) #calculate result
        print(str(i) + " + " + str(i+1) + " + " + str(i+2) + " = " + str(result)) #print each equation

#get user input and call the function to display equations
start_number = input("Enter a start number: ")
end_number = input("Enter an end number: ") 
print()
display_equations(start_number, end_number)

# Question 3

print()
print("Question 3")
print()

def generate_student_number(student_type):

    number_code = "" #define empty string

    #generate random 7 number code
    for i in range(0, 7):
        random_number = random.randint(0, 9)
        number_code = number_code + str(random_number)
    
    #if cases to produce respective student codes
    if(student_type == "U"):
        student_number = "U" + number_code
    
    if(student_type == "P"):
        student_number = "P" + number_code

    if(student_type == "F"):
        student_number = "F" + number_code

    return student_number

#while loop to get user input and quit when QUIT is input
while True:
    user_input = input("Enter student type (U/P/F or QUIT): ")

    if(user_input == "QUIT"): 
        print("Good bye!")
        break

    print("Student number generated: " + generate_student_number(user_input))
    print()

# Question 4

print()
print("Question 4")
print()

#define function that takes a string as an argument
def filter_digit(sentence):  
    digit_string = "" #define empty string
    digit_sum = 0 #define sum starting at 0

    #loop through sentence to find digits and add them to string
    for i in range(0, len(sentence)): 
        for j in range(0, 10):
            if(sentence[i] == str(j)):
                digit_string = digit_string + sentence[i]
                digit_sum += int(sentence[i])

    return digit_string, digit_sum

#gather user input and pass into function
user_input = input("Enter a sentence: ")
print()
digit_string, digit_sum = filter_digit(user_input)
print("Digit string: " + digit_string)
print("Sum: " + str(digit_sum))
    