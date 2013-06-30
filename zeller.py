# Greg Smyth
# MOOC Wk2 homework optional 1
# 30th June 2013
# zellers.py

print("Enter a date in the format DD MM YYYY:")
zeller_day=input("Day: ")
zeller_month=input("Month: ")
zeller_year=raw_input("Year: ")


A=zeller_month-2
B=zeller_day
C=int(zeller_year[2:])
D=int(zeller_year[:2])

if A<=0:
    A=A+12
    C=C-1




W=(13*A-1)/5
X=C/4
Y=D/4
Z=W+X+Y+B+C-2*D

R= Z%7

print R
days_array=["Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"]

print "That was a", days_array[R]+"day"
