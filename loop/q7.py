number=int(input("Enter any number"))
i=1
num=0
innernum=0
count=0
while i<=number:
    num=i
    innernum=1
    count=0
    while innernum < num:
        if num%innernum == 0:
            count = count+innernum
        innernum=innernum+1
    if count == num:
        print("the given number is perfect number",num)
    i=i+1
