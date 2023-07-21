list_a = [1,2,3,4]
list_b = ['a', 'b', 'c', 'd']
list_c = [99, 88, 77, 66]

zipped = zip(list_a, list_b, list_c)
zipped_list = list(zipped)

print(zipped_list)