#Bryce Kepple
#9/4/24
#2 Interest lab
# Intro to Comp Sci


#gets starting amount of money as float from user
principal=float(input("Enter the principal value:"))

#gets the interest rate as a float from user
interest_rate=float(input("Enter the interest rate:"))

#finds the interest earned and prints it
interest=interest_rate*principal
print(f"the interest earned is ${interest:.2f}")

#finds the total amount of money after year one and prints it
principal_year1=principal+interest
print(f"the value of the investment after one year is ${principal_year1:.2f}")

#calculates the interest earned per a month and prints it
avg_monthly_interest=interest/12
print(f"the average interest is ${avg_monthly_interest:.2f}")
