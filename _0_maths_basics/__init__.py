list1 = [4, 6, 3, 24, 2, 14, 10, 7]


def bubble_sort(li):
    le = len(li)
    temp = False
    for i in range(le - 1):
        for j in range(0, le - i - 1):
            if li[j] > li[j + 1]:
                temp = True
                li[j], li[j + 1] = li[j + 1], li[j]
    print("After sorting : ", li)


def bubble_sort(li):
    le = len(li)
    for ind in range(le - 1, 0, -1):
        for ind2 in range(ind):
            if li[ind2] < li[ind2 + 1]:
                temp = li[ind2]
                li[ind2] = li[ind2 + 1]
                li[ind2 + 1] = temp
    print("After reverse sorting : ", li)


bubble_sort(list1)

'''
select distinct salary from employee
order by salary
desc limit 1
offset 2;


'''