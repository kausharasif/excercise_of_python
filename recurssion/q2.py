x=[]
def AmountToDigits(number):
    global x
    if number !=0:
        mod = number%10
        if mod==1:
            x.append("one")
        elif mod ==2:
            x.append("two")
        elif mod ==3:
           x.append("three")
        elif mod ==4:
            x.append("four")
        elif mod==5:
            x.append("five")
        elif mod==6:
            x.append("six")
        elif mod==7:
            x.append("seven")
        elif mod==8:
            x.append("eight")
        else:
           x.append("nine")
        AmountToDigits(number//10)
        return x
    else:
       return None


number=int(input("enter number"))
AmountToDigits(number)
length = len(x)
i = length -1
print(len(x))
while i>=0:
    print(x[i],end=' ')
    i=i-1
