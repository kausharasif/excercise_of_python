number=int(input("Enter any number to find out prime number in a given range"))
i=1
num=0
outernum=1
count =0
while i <= number:
    num=i
    outernum=1
    count =0
    while outernum <= num:
        if num%outernum ==0:
            count = count+1
        outernum=outernum+1
    if count == 2:
        print("the given number is prime",i)
    i=i+1

