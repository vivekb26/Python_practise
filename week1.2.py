def accordian(list_1):
    list_2 = []
    for i in range(len(list_1)-1):
        diff = abs(list_1[i] - list_1[i+1])
        list_2.append(diff)
    print(list_2)
    # increase_decrease(list_2)

# def increase_decrease(list_2):
#     valid =True
#     for i in range(len(list_2)-1):
#         if list_2[i] < list_2[i+1]:
#             print("1")
#             if list_2[i+1] > list_2[i+2]:
#                 print("2")
#                 increase_decrease()
#             else:
#                 valid = False
#                 print("3")
#                 break
#         elif list_2[i] > list_2[i+1]:
#             print("4")
#             if list_2[i+1] < list_2[i+2]:
#                 print("5")
#                 increase_decrease()
#             else:
#                 valid = False
#                 print("6")
#                 break
#         else :
#             valid = False
#             print("7")
#             break
#     print(valid)


    if list_2[i] < list_2[i+1]:
        dec_1()
    elif list_2[i] > list_2[i+1]:
        inc_1()


def inc_1():
    if list_2[i] < list_2[i+1]:
        

def dec_1():
    if list_2[i] > list_2[i+1]:
        inc_1()
list_1 = [1,5,1]
list_2 = [1,5,2,8,3]
accordian(list_2)