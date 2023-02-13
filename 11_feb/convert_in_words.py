Ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
Tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

amount = int(input('Enter the amount: '))

def format_input_amount(amount):
    """
    This function is used to format the amount
    ex :25
    Rs: 25.00
    :param amountz
    """
    return f"{amount}.00"

def convert_to_words(func,amt):
        for_amount = func(amt)  # function uses another function 
        n = int(float(for_amount))
        print(type(n))
        if n>99999:   
             print("Cant solve for more than 5 digits")
        else:   
            digit=[0,0,0,0,0]                    
            i=0
            while n>0:
                digit[i]=n%10
                i+=1
                n=n//10                         # input the number in list d []
            num=""
            if digit[4]!=0:                      # ex : 34567 d =[7,6,5,4,3]
                if(digit[4]==1):                 
                    num+=Tens[digit[3]]+ " Thousand "    # third element of list
                else:
                    num+=nty[digit[4]]+" "+Ones[digit[3]]+  " Thousand "    #combining the last and third words of list 
            else:
                if digit[3]!=0:
                    num+=Ones[digit[3]]+ " Thousand " # if last element is zero
            if digit[2]!=0:                                          
                num+=Ones[digit[2]]+" Hundred "
            if digit[1] != 0:                          # for first 2 digits for d list
                if (digit[1] == 1):
                    num += Tens[digit[0]]
                else:
                    num += nty[digit[1]] + " " + Ones[digit[0]]
            else:
                if digit[0] != 0:
                    num += Ones[digit[0]]

        return num   

div = convert_to_words(format_input_amount,amount)
print(div)