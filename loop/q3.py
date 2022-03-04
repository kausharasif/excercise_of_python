number = int(input("Enter any number"))
i=1
count =0
while i <= number:
    if number % i == 0:
        count = count+1
    i = i+1

if count > 2:
    print("The number is composite number",number)
else:
    print("The number is not composite number",number)