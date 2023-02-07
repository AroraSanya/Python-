notes=[500,200,50,20,10]
amount=int(input("enter the amount"))
def total_number(amount,notes):
    for note in notes:
        count=0
        if amount>=note:
            if note==500:
                count=amount// note
                amount=amount%note
            elif note==200:
                count=amount// note
                amount=amount% note
            elif  note==50:
                count=amount// note
                amount=amount% note
            elif note==20:
                count=amount// note
                amount=amount% note
            elif note==10:
                count=amount// note
                amount=amount% note
            print("total no. of {}: is {}".format(note,count))
        else:
            print("total no. of {}: is {}".format(note,count))
total_number(amount,notes)            
    





