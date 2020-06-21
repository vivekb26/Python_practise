def expanding(list_1):
    list_2 = []
    for i in range(len(list_1)-1):
        diff = list_1[i] - list_1[i+1]
        list_2.append(abs(diff))
    # print(list_2)
    valid = True
    for i in range(len(list_2)-1):
        if list_2[i] >= list_2[i+1]:
            valid = False
    print(valid)

list_1 = [1,3,7,2,9]
list_3 = [1,3,7,2,-3]
list_4 = [1,3,7,10]
expanding(list_4)