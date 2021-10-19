# Binary Search Algorithm

"""Creating a list to generate a random number in between 1 and 100"""

from random import randint

rand_list = []
for i in range(0 , 10):
    rand = randint(0 , 10)
    rand_list.append(rand)
    rand_list.sort()

n = int(input('Please enter a number of your choice: '))
min = 0
max = len(rand_list)
print(max)
print(rand_list)

def binarysearch(rand_list, min, max, n):
    if max >= min:
        median = (max + min)//2

        if n == rand_list[median]:
            return n
        elif n < rand_list[median]:
            return binarysearch(rand_list, 0, median - 1, n)
        else:
            return binarysearch(rand_list, median + 1, max, n)
    else:
        return "NA"

index = binarysearch(rand_list, 0, max-1, n)


if index != "NA":
    print(f'Number is available at {index} in the list')
else:
    print('Number is not in the list!')

