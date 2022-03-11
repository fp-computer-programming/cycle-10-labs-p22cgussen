# Author: CCG 3/10/22

def num(number):
    x = 1
    output = 0
    while x <= number:
        output += x
        x += 1
    return output

print(num(10))
print(num(5))
print(num(3))
