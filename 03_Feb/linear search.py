def search(list,n):
    for i in range(len(list)):
        if list[i] ==  n:  
            return i 
    return -1
                


list=[2,4,55,6]
n=int(input("enter the number:"))
res = search(list,n) 
if res == -1:
    print("not found")  
else:
    print(res)