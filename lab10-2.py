# Author: CCG 3/10/22

def num(lst):
    ans = []
    for x in lst:
        if(x > 500):
            break
        elif x % 5 == 0 and x <= 150:
            ans.append(x)
    return ans


print(num([20, 150, 21, 145, 200, 151]))
