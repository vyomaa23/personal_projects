# Binary Search Algorithm

"""Creating a list to generate a random number in between 1 and 100"""

from random import randint

rand_list = []
for i in range(1, 100):
    rand = randint(1, 100)
    rand_list.append(rand)

print(rand_list)
user_in = input("Please input a number: ")
search_flag = True

while search_flag:
    long = int(len(rand_list))
    l1 = rand_list[1:long]
    print(l1)
    if user_in in l1:
        print('Value Found!')
        search_flag = False
        print(f'Searched Value: {user_in}')
    else:
        print(f'Searched Value: {user_in}')
        search_flag = False


# if user_in in rand_list[]:
#     print("Yes, it's present")
# else:
#     print("Number isn't available34")
