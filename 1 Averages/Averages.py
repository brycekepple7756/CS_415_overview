#Bryce Kepple
#9/3/2024
#1 Averages lab
#Intro to computer science

#sets grade weight values to different variables
participation=.15
test=.45
projects=.40
#uses float input to get students participation grade
part_grade=float(input("Enter the student's participation grade."))

#gets the test grades as ints
test1=float(input("Enter the student's first test grade."))

test2=float(input("Enter the student's second test grade."))

test3=float(input("Enter the student's third test grade."))

#sets average of the test grades to a variable and then prints it
test_average=(test1+test2+test3)/3

print(f"Test average: {test_average:.2f}")

#gets the project grades as ints
proj1=float(input("Enter the student's first project grade."))

proj2=float(input("Enter the student's second project grade."))

#sets average of the project grades to a variable and prints it
proj_average=(proj1+proj2)/2

print(f"Project average: {proj_average:.2f}")
#weighs the grades and adds them together to get final grade in the class and print it
final_grade=(participation*part_grade)+(test*test_average)+(projects*proj_average)

print(f"Final grade: {final_grade:.2f}")

