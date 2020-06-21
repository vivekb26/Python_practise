n = 5
# # for octave
# o_li =[]
# def octave(number) :
#     if number > 7:
#         o = number % 8
#         o= o + ((number // 8)*10)
#         o_li.append(o)
#         number= number // 8
#     else :
#         o_li.append(number)
# for binary
b_li =[]
def binary(number) :
    s = 0
    sum = 0
    li = []
    while number > 1:
        o = number % 2
        li.append(o)
        number //= 2
        s+=1
    li.append(number)
    li.reverse()
    for i in range(len(li)):
        sum = sum + ( li[i] * (10**s))
    print(sum)
    print(li)

# for i in range(26):
binary(25)
    # octave(i)
# print (b_li)




# print("{} {} {} {}".format())