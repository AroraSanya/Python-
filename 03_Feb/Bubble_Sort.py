def sort(array):
    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array          
array=[3,4,5,6,1]
n=len(array)
print(sort(array))