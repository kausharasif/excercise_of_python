number = int(input("Enter any number"))
total=0
num=0
while number>=1 :
    num=number%10
    total=total+num
    number=number//10

print("The sum of given number is",total)


