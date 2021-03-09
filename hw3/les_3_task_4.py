import random
my_list = [random.randint(0,99) for _ in (range(10))]
max_count = 0
for first_num in range(10):
    count = 0
    for second_num in range(10):
        if my_list[first_num] == my_list[second_num]:
            count += 1
        if count > max_count:
            max_count = count
            num = my_list[first_num]
if max_count > 1:
    print(f'{max_count} раза встречается число {num}')
else:
    print('все элементы уникальны')
print(*my_list)
