def MinimumNumber(*numbers):
    location = 0
    length = len(numbers)
    i = 0
    while i<length:
        if numbers[i] < numbers[location]:
            location = i
        i=i+1
    print("The minimum value from the given list is",numbers[location])

MinimumNumber(100,48,78,-1,2,0)