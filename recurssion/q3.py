def DecimalToHexadecimal(number):
    if number>0:
        remainder = number%16
        number = number//16
        DecimalToHexadecimal(number)
        print(remainder,end='')
    else :
        return None

number = int(input("Enter Number"))
DecimalToHexadecimal(number)

