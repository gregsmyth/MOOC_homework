# Name: Greg Smyth
# Homework MOOC Wk2
# wk2_loops.py
# 28th June 2013

print("MOOC Week 2 Homework")
print("Exercise 1.8")
print("Part 1")

for n in range(1,10):
    print(1.0/n)


#Exercise 1.8 Part 2

print("Part 2")
number=input("Enter a positive number: ")
if number < 0:
    print ("That's a negative number")
else:
    while number >=0:
        print number
        number-=1

#Exercise 1.8 Part 3

print("Part 3")

base=input("Enter a base: ")
exp=input("Enter an exponent: ")
ans=base**exp
print ans

#Exercise 1.8 Part 4

print("Part 4")

number=input("Enter an even number: ")
while (number%2)!=0:
    number=input("Enter an even number: ")
new_number=number/2.0
print("Congratulations, your number is divisible by 2")
print str(number) +"/2 = "+ str(new_number)

