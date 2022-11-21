initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(f'Initial list: {initial_list}')

asc_sorted_list = sorted(initial_list)
print(f'Ascendent sorted list: {asc_sorted_list}')

desc_sorted_list = sorted(initial_list, reverse=True)
print(f'Descendent sorted list: {desc_sorted_list}')


print(f'Even indexed elements: {initial_list[::2]}')

print(f'Odd indexed elements: {initial_list[1::2]}')

multiple_of_three = [elem for elem in initial_list if elem % 3 == 0]
print(f'Multiple of 3 elements: {multiple_of_three}')