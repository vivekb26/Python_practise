def print_sum(list_1):
    sum = 0
    for i in list_1:
        if is_prime(i):
            sum = sum + i
            print(i)
    print(sum)

def is_prime(number):
    if number == 1 or number == 0:
        return False
    elif number == 2 :
                return True
    else:
        for i in range(2,number):
            if number == 2 :
                return True
            elif (number % i) != 0 :
                return True
            else:
                return False 


print_sum([1,2,3,4,5,7,10,11])