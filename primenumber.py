Number=int(input('Please Enter any Number: (bigger or equal than 2)'))
n=0

factor=2
if Number < 2:
    print("error")
else :

    print ("the factor is : " , Number)
    factor =2
    while factor <= Number :
        if Number % factor ==0 :
            print(factor)
            Number = Number//factor
            n += 1
        else:
            factor += 1
    if n == 1 :
        print('is prime number')
