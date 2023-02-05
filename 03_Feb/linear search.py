def search(list,n):
    for i in range(len(list)):
        if list[i] ==  n:
            print("Number is present at ",i) 
    return print("Number is  not present ") 
                


list=[2,4,55,6]
n=int(input("enter the number:"))
search(list,n)   