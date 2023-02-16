
 #Implement function overloading
# def multipli(a,b):
#     return a*b
# def multipli(a,b,c):
#     return a*b*c 
# mul=multipli(2,4,5)
# print (mul)
# *****************
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# add_obj=add(2,3,5,6,6,7)
# print(add_obj)
def add(**kwargs):
    sum=0
    for value in kwargs.items():
        sum=sum+value
    return sum
add_obj=add(2,5)
print(add_obj)


