# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to
# length.

# Function.

def listOfMultiples(num, length):
    lst = list()
    if num and length > 0:
        for i in range(1, length + 1):
            x = num * i
            lst.append(x)

    return lst


# Test

a = listOfMultiples(2, 7)
print(a)
