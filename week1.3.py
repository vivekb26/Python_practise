def rotate(list_1):
    list_3 = []
    for i in range(len(list_1)):
        list_2 =[]
        for j in range(len(list_1)):
            n = list_1[j][i]
            # print(n)
            list_2.append(n,)
            # print("l2" ,list_2)
        (list_2.reverse())
        list_3.append(list_2)
        # print(list_3)
    print(list_3)

rotate([[1,2,3],[4,5,6],[7,8,9]])
# answer 7 4 1 , 8 5 2, 9 6 3