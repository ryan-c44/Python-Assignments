# Ryan Castles, 6433236, CSIT110

#Question 1

print("Question 1. \n")

#Create input variables
assignment_mark = input("Enter your assignment mark: ")
project_mark = input("Enter your project mark: ")
final_exam = input("Enter your final exam mark: ")

#Convert final exam input to an integer
final_exam_mark = int(final_exam)
total = int(assignment_mark) + int(project_mark) + int(final_exam)

#If/else state to acquire grade based on marks
if final_exam_mark >= 20:
    if total >= 80:
        grade = 'A'
    elif total >= 60:
        grade = 'B'
    elif total >= 50:
        grade = 'C'
    elif total < 50:
        grade = 'Fail'
else:
    grade = "Fail"


print()

#Print results using formatting
print("Your result: \n")
print("{0:<10}{1:>8}".format("Assignment: ", assignment_mark))
print("{0:<10}{1:>10}".format("Project: ", project_mark))
print("{0:<10}{1:>8}".format("Final exam: ", final_exam))
print("{0:<10}{1:>10}".format("Total: ", total))
print("{0:<10}{1:>10}".format("Grade: ", grade))

print()

#Question 2

print("Question 2. \n")

#Assign options to variables
option1 = "Green eggs and ham"
option2 = "Red breads with jam"
option3 = "Blue salad with lamb chops"

print("Breakfast menu at Whosville Eatery")
print("1) " + option1)
print("2) " + option2)
print("3) " + option3)

#Get user input for selection
breakfast_selection = input("Enter your selection (1/2/3): ")
print()
#convert selection to an integer
selection = int(breakfast_selection)

#If / else to determine the selection made based on input
if selection == 1:
    breakfast = option1
elif selection == 2:
    breakfast = option2
elif selection == 3:
    breakfast = option3
else:
    breakfast = "Not an option"

#declare variables and assign them to size of drinks
size_small = "small"
size_medium = "medium"
size_large = "large"

print("Drink size:")
print("{0:<10}{1:>10}{2:>10}".format("S) Small", "M) Medium", "L) Large"))  #Use formatting here
size_selection = input("Enter your selection (S/M/L): ")
print()

#Check user input and assign size based on character input
if(size_selection == "S"):
    drink_size = size_small
elif(size_selection == "M"):
    drink_size = size_medium
elif(size_selection == "L"):
    drink_size = size_large
else:
    drink_size = "Unknown size"

print("Your order is " + breakfast + " and a " + drink_size + " drink.")

print()

#Question 3

print("Question 3. \n")

#Get the user input either U or P
student_type_char = input("Enter student type (postgrad/undergrad)? P/U: ")

#Ask for postgrad info if input was 'P'
if student_type_char == 'P':
    student_type = "Postgraduate"
    thesis_title = input("Enter thesis title: ")
    supervisor = input("Enter supervisor: ")
    co_supervisor = input("Enter co-supervisor: ")

    print()
    
    print("Enrolment information:")
    print("{0:<10}{1:>20}".format("Student type: ", student_type))
    print("{0:<20}{1:>25}".format("Thesis title: ", thesis_title))
    print("{0:<17}{1:>20}".format("Supervisor: ", supervisor))
    print("{0:<15}{1:>22}".format("Co-supervisor: ", co_supervisor))

#Else if input was 'U' ask questions relating to undergrad student
elif student_type_char == 'U':
    student_type = "Undergraduate"
    subject_1 = input("Enter 1st subject: ")
    subject_2 = input("Enter 2nd subject: ")
    subject_3 = input("Enter 3rd subject: ")
    subject_4 = input("Enter 4th subject: ")

    print()

    print("Enrolment information:")
    print("{0:<10}{1:>18}".format("Student type: ", student_type))
    print("{0:<10}{1:>15}".format("Subject 1: ", subject_1))
    print("{0:<10}{1:>13}".format("Subject 2: ", subject_2))
    print("{0:<10}{1:>15}".format("Subject 3: ", subject_3))
    print("{0:<10}{1:>15}".format("Subject 4: ", subject_4))

else:
    student_type = "Invalid"


print()

#Question 4

print("Question 4. \n")

#Assign variables relating to journal names
commodity_markets = "Journal of Commodity Markets"
sustainable_mining = "Journal of Sustainable Mining"
asia_pacific = "Journal of Asia-Pacific Biodiversity"
geometry = "Journal of Geometry"
algebra = "Journal of Algebra"
number_theory = "Journal of Number Theory"
total_cost = 0
selections = "Your selection: \n"



#Format the information with their price

print("{0:<25}{1:>21}".format(commodity_markets, "$31"))
print("{0:<25}{1:>20}".format(sustainable_mining, "$32"))
print("{0:<25}{1:>13}".format(asia_pacific, "$33"))
print("{0:<25}{1:>24}".format(geometry, "$25"))
print("{0:<25}{1:>24}".format(algebra, "$27"))
print("{0:<25}{1:>24}".format(number_theory, "$29"))

print()

#Get user input to determine if they want to buy journal or not
selection1 = input("Subscribe to " + commodity_markets + "? (Y/N): ")
selection2 = input("Subscribe to " + sustainable_mining + "? (Y/N): ")
selection3 = input("Subscribe to " + asia_pacific + "? (Y/N): ")
selection4 = input("Subscribe to " + geometry + "? (Y/N): ")
selection5 = input("Subscribe to " + algebra + "? (Y/N): ")
selection6 = input("Subscribe to " + number_theory + "? (Y/N): ")

#If input is 'Y' add to selection and add onto total price
if selection1 == 'Y':
    total_cost += 31
    selections += " - " + commodity_markets + " ($31) \n"
if selection2 == 'Y':
    total_cost += 32
    selections += " - " + sustainable_mining + " ($32) \n"
if selection3 == 'Y':
    total_cost += 33
    selections += " - " + asia_pacific + " ($33) \n"
if selection4 == 'Y':
    total_cost += 25
    selections += " - " + geometry + " ($25) \n"
if selection5 == 'Y':
    total_cost += 27
    selections += " - " + algebra + " ($27) \n"
if selection6 == 'Y':
    total_cost += 29
    selections += " - " + number_theory + " ($29) \n"

#If input is 'N' for all, selections will be none.
if((selection1 == 'N') & (selection2 == 'N') & (selection3 == 'N') & (selection4 == 'N') & (selection5 == 'N') & (selection6 == 'N')):
    selections += " - None \n"

print()

#print selections and total price
print(selections)
print("Total cost ${0}".format(total_cost))



