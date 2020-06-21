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
    d= number
    if number <16:
        s= s+1
        if (number < 10):
            o = ((number%16))
            li.append(o)
            number = number //16
            
        elif (number ==10):
            li.append('0A')
        elif (number ==11):
            li.append('0B')
        elif (number ==12):
            li.append('0C')
        elif (number ==13):
            li.append('0D')
        elif (number ==14):
            li.append('0E')
        elif (number ==15):
            li.append('0F')
    elif number >=16:
        s=s+1
        if (number // 16) <10:
          s1=number//16
        elif (number//16)==10:
            s1="A"
        elif (number//16)==11:  
            s1="B"
        elif (number//16)==12:
            s1="C"
        elif (number//16)==13:
            s1="D"
        elif (number//16)==14:
            s1="E"
        elif (number//16)==15:
            s1="F"
        # s1=number // 16
        # print(s)
        if (number%16)<10:
            o = ((number % 16)+((number//16)*(10**s)))
            li.append(o)
            number = number // 16
        # s=number // 16
        elif (number%16)==10:
            li.append(str(s1) +'A')
        elif (number%16)==11:
            li.append(str(s1)+'B')
        elif (number%16)==12:
            li.append(str(s1)+'C')
        elif (number%16)==13:
            li.append(str(s1)+'D')
        elif (number%16)==14:
            li.append(str(s1)+'E')
        elif (number%16)==15:
            li.append(str(s1)+'F')
    return(li[d-1])
    
    # print(li)
# print(ary(20,2))

s=0
for i in range(1,200):
    # print(i)
    print ("{0}\t{1}\t{2}\t{3}".format(i, ary(i,8),(hex(i)) , ary(i,2)))
    # print(i,end=" ")
    # print(ary(i,2),end=" ")
    # (hex(i))
    # print(li)
    
