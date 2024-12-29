#
#Bryce Kepple
#Pay Stub Assignment
#gather input from user and make 2 calculations
#

# using input with eval or float to gather data
employee_name=input("Enter your name: ")

anniversary_month=eval(input("Enter month hired (1-12): "))

anniversary_year=eval(input("Enter year hired: "))

hours_worked=eval(input("Enter hours worked(0-350): "))

job_title=input("Enter your job title: ")

hourly_pay_rate=float(input("Enter your hourly pay rate: "))

#formatting the anniversary to be in mm/yyyy format
anniversary=str(anniversary_month)+"/"+str(anniversary_year)

#calculations

#months worked: finds how many years worked, converts to months, adds nine for the current month and then subtracts the month joined
years_worked=(2024-anniversary_year)
months_worked=((years_worked*12)+9-anniversary_month)


#vacation hours earned: times the amount of months worked by the rate that hours are earned (8.25)
vacation_hours=months_worked*8.25


#gross pay: hourly pay times hours worked
gross_pay=(hourly_pay_rate*hours_worked)


#retirement: gross pay times retirement percentage (5.2%)
retirement_withholding=(gross_pay*.052)


#tax: gross pay minus retirement times tax rate (28%)
tax_withholding=(gross_pay-retirement_withholding)*.28


#net pay: total pay minus retirement and taxes
net_pay=(gross_pay-retirement_withholding-tax_withholding)


#display
#used to print a line of 42 equal signs
print("="*42)

#uses " "*x to print a certain number of spaces, and then adds comp name and logo over many lines
print((" "*6)+"Gekko & Co.")
print((" "*10)+"\"$\"")
print((" "*10)+"~~~")
print((" "*9)+"/  \\ `.")
print((" "*8)+"/    \\  /")
print((" "*7)+"/_ _ _ \\/")
print()
print("-"*42)


#uses f and : <16s to format the outputs so the second value is lined up
print(f"{'Pay period:' : <16s}{'9/2024'}")
print(f"{'Name:' : <16s}{employee_name}")
print(f"{'Title::' : <16s}{job_title}")
print(f"{'Anniversary:' : <16s}{anniversary}")
print(f"{'Months Worked:': <16s}{months_worked}{' months'}")
print(f"{'Vacation hours:' : <16s}{vacation_hours:.2f}")
print("-"*42)


#does same as above but has a $ added before the money amounts
print(f"{'Gross pay:' : <16s}{'$ '}{gross_pay:.2f}")
print(f"{'Retirement:' : <16s}{'$ '}{retirement_withholding:.2f}")
print(f"{'Tax:' : <16s}{'$ '}{tax_withholding:.2f}")
print("-"*24)
print(f"{'Net pay:' : <16s}{'$ '}{net_pay:.2f}")
print("="*42)
