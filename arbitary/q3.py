import math
def ArmstrongNumber(*numbers):
    length = len(numbers)
    i = 0
    while i<length:
        exponent = len(str(numbers[i]))
        total =0
        copy_number = numbers[i]
        while copy_number > 0:
            reminder = copy_number%10
            temp = math.pow(reminder,exponent)
            total += temp
            copy_number = int(copy_number/10)
        if numbers[i] == total:
            print(f"{numbers[i]} is armstrong number")
        else:
              print(f"{numbers[i]} is not armstrong number")
        i=i+1

ArmstrongNumber(153,398,370,371,407)