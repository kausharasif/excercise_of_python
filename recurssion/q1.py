sem=1
octal=0
def DecimalToOctal(number):
    global sem,octal
    if number!= 0:
        octal=octal+(number%8)*sem
        sem=sem*10
        DecimalToOctal(number//8)
        '''print(octal,end= ' ')'''
        return octal
    else:
        return None #to break the recurssion

number = int(input("Enter number"))
print("Octal value of decimal number is",DecimalToOctal(number))
    
