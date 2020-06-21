# def binary(number):
#     s=0
#     d=0
#     o=0

#     while number >1:
#         o = o + ( (number % 2) * 10 ** s)
#         number = number //2
#         s= s+1
#     o = o + ( (number) * 10 ** s)
#     print (o)


def ary(number,d):
        s=0
        o=0
        # d=2

        while number >=d:
            o = o + ( (number % d) * 10 ** s)
            number = number //d
            s= s+1
        o = o + ( (number) * 10 ** s)
        # print (o)
        return o
li =[]
def hex(number):
    o=0
    s=0
    # li =[]
    while number >=16:
        if 0< (number%16)<10 or 0 <(number <10):
            o = (o+(number//16)*(10**s))
            li.append(o)
            number = number // 16
            s= s+1
        elif (number%16)==10 or (number ==10):
            li.append('A')
        elif (number%16)==11 or (number ==11):
            li.append('B')
        elif (number%16)==12 or (number ==12):
            li.append('C')
        elif (number%16)==13 or (number ==13):
            li.append('D')
        elif (number%16)==14 or (number ==14):
            li.append('E')
        elif (number%16)==15 or (number ==15):
            li.append('F')
        elif (number%16)==0 or (number ==0):
            s+=1
            li.append((o+(number//16)*(10**s)))
    if (number % 16)< 10 or (number < 10):
        o = ((number%16)*(10**s))
        li.append(o)
        number = number //16
        s= s+1
    elif (number%16)==10 or (number ==10):
            li.append('A')
    elif (number%16)==11 or (number ==11):
            li.append('B')
    elif (number%16)==12 or (number ==12):
            li.append('C')
    elif (number%16)==13 or (number ==13):
            li.append('D')
    elif (number%16)==14 or (number ==14):
            li.append('E')
    elif (number%16)==15 or (number ==15):
            li.append('F')
    print(li)
# print(li)
# print(ary(20,2))


# for i in range(1,18):
#     print ("{0} {1} {2}".format(i, ary(i,8), ary(i,2)),end =" ")
#     # print(ary(i,1))
#     # print(ary(i,2))
(hex(16))
    
