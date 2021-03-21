# list of multiples of 5

import random
# first option
print('1 option')
new_list = [*range(5,50,5)]
print(new_list)
print('Minimum', min(new_list), 'Maximum', max(new_list), 'Total', sum(new_list))

# second option
print('2 option')
new_list2 = []
for i in range(10):
    new_list2.append(random.randint(1,100) * 5)
print(new_list2)
print('Minimum', min(new_list), 'Maximum', max(new_list), 'Total', sum(new_list))