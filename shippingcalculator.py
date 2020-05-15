def ship(num):
    if num >0:
        return '%.2f' % (2.95*(num-1)+10.95)
    else :
        return "errow"


a = int(input('number of package'))
print (ship(a))