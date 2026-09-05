def average_number(*args):
    total =0
    average=0
    for num in args:
        total += num

    average=total/len(args)
    return average

x=average_number(10,20,30,40)
print(x)