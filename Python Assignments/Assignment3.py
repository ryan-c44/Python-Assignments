# Ryan Castles, 6433236, CSIT110

# Question 1

print("Question 1")

print()

#Take user input for upper bound and gap
upper_bound = input("Enter upper bound: ")
gap = input("Enter gap: ")
print()

#total starts at 0
total = 0

print("Go forward: ", end="")

#For loop to go forward through each integer with respective gap to upper bound
for i in range(0, int(upper_bound) + 1, int(gap)):
    if(i < int(upper_bound)):
        trailing = ", "
    
    if(i + int(gap) > int(upper_bound)):
        trailing = "."

    print(i, end="")
    print(trailing, end="")

    total = total + i 


print("\nSum of numbers = " + str(total))

total = 0

print()

print("Go backward: ", end="")

#For loop decrementing (going backwards)
for i in range(int(upper_bound), 0 - 1, -int(gap)):
    if(i > 0):
        trailing = ", "
    
    if(i - int(gap) < 0):
        trailing = "."

    print(i, end="")
    print(trailing, end="")  

    total = total + i

print("\nSum of numbers = " + str(total))
print()


# Question 2

print("Question 2")

number = input("Enter a number (1-9): ") 
print()

#forward loop
print("Go forward: ")

for i in range(1, int(number) + 1):
    print(i, end="")
    for j in range(0, i):
        print("?", end="")
    print()

print()

#backward loop
print("Go backward: ")

for i in range(int(number), 0, -1):
    for j in range(i, 0, -1):
        print("-", end="")
    print(i)

print()

# Question 3

print("Question 3")
print()

#Take user input for min and max integers
min_int = input("Enter the minimum integer: ")
max_int = input("Enter the maximum integer: ")

print()

#format the data
print("{0:<8}{1:>10}{2:>10}".format("Number", "Sign", "Parity"))

#Loop through to check parity and postive or even
for i in range(int(min_int), int(max_int) + 1):
    if(i % 2 == 0):
        parity = "Even"
    else:
        parity = "Odd"

    if(i < 0):
        sign = "Negative"
    elif(i == 0):
        sign = "Zero"
    else:
        sign = "Positive"

    print("{0:>6}{1:>12}{2:>10}".format(i, sign, parity))

print()

# Question 4

print("Question 4")
print()

#take user input for sentence and letter
sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

print()

#format the data
print("{0:<8}{1:>10}{2:>15}{3:>15}".format("Index", "Letter", "Matched", "Counting")) 

index = 0
count = 0

#loop through sentence to get indexes
for i in range(0, len(sentence)):
    index += 1

#loop through each letter and find matches, increasing the count if there is one
for i in range(0, index):

    if(sentence[i] == letter.lower() or sentence[i] == letter.upper()):
        matched = "Yes"
        count += 1
    else:
        matched = "No"

    print("{0:>5}{1:>13}{2:>15}{3:>15}".format(i, sentence[i], matched, count))

print()

print("Letter matched count: " + str(count))

