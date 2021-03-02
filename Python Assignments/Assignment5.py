# Ryan Castles, 6433236, CSIT110

import random

#Question 1

print("Question 1")
print()

#function to create list of odd numbers
def create_odd_list(number_elements):
    odd = []
    num = 0
    i=1

    #while loop to append list until input amount is reached with odd numbers
    while num < int(number_elements):
        odd.append(i)
        i+=2
        num+=1

    return odd #return the list

#function to create list of negative numbers
def create_negative_list(number_elements):
    negative = []
    num = 0
    i = -2

    #while loop to append list until input amount is reached with negative even numbers
    while num < int(number_elements):
        negative.append(i)
        i -= 2
        num+=1

    return negative

#Get user input for amount of numbers in list
numbers = input("How many numbers to put into lists? ")
print()

#print the two lists by calling the respective functions
print("Here are the 2 lists:")
print("Odd number list: " + str(create_odd_list(numbers)))
print("Negative even number list: " + str(create_negative_list(numbers)))

#Question 2

print()
print("Question 2")
print()

#define a function that creates and prints subject list
def subject_function(number):
    i = 1
    total = 0
    subject_list = []
    credit_point_list = []

    #while loop to take user input until amount of subjects is reached
    while(i <= int(number)):
        subject = input("Enter subject " + str(i) + ": ")
        cp = input("Enter subject " + str(i) + " credit point: ")
        print()

        subject_list.append(subject)
        credit_point_list.append(str(cp))
        i+=1
        total+=int(cp)

    #format and print the subjects
    print("Selected subjects:")
    print("{0:<10}{1:>10}".format("Subject", "CP"))
    for i in range(0, int(number)):
        print("{0:<10}{1:>10}".format(subject_list[i], credit_point_list[i]))
    
    print("{0:<10}{1:>10}".format("Total cp:", total))

#Ask for user input and call function to print
subject_amount = input("How many subjects do you want to enrol? ")
print()
#call function to print subject list
subject_function(subject_amount)

#Question 3

print()
print("Question 3")
print()

#get user input for amount of numbers to be in list
numbers_in_list = input("How many numbers are in the list? ")

i = 1
list_elements = [] #define a list of elements

#while loop to get elements to append to list
while(i <= int(numbers_in_list)):
    element = input("Enter list element: ")
    list_elements.append(element)
    i += 1

#print the formatted list
print()
print("You have entered: ")
print("{0:<10}{1:<10}{2:<10}".format("Index", "List", "Reverse"))

x = 0
j = len(list_elements) - 1

while(x <= len(list_elements) and j >= 0):
    print("{0:<10}{1:<10}{2:<10}".format(x, list_elements[x], list_elements[j]))
    x+=1
    j-=1
    

#Question 4

print()
print("Question 4")
print()

def generate_random_name():

    last_names = ["Smith", "Black", "White", "Jerry", "Allen", "Dong", "Castles", "Tonien", "Windle", "Connelly"]
    first_names = ["Ryan", "Jim", "John", "Charlies", "Chuck", "Mat", "Tim", "Jerry", "Sarah", "Jess"]

    #randomise index each loop to return different names
    random_index_first = random.randint(0, len(last_names) - 1)
    random_index_last = random.randint(0, len(last_names) - 1)
        
    first = first_names[random_index_first]
    last = last_names[random_index_last]

    return first, last

#while loop to generate different names each loop
while True:   
    first, last = generate_random_name() #get values returned from function and store to variables
    user_input = input("Press Enter to generate random name, or type QUIT to quit: ")
    #generate name if Enter is pressed
    if(user_input == ""):
        print("Name generated: " + first + " " + last) 
        print()
    
    #break loop if user types QUIT
    if(user_input == "QUIT"):
        print("Good bye!")
        break