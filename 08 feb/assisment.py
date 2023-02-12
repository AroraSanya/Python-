import datetime
def registered_detailed():
    first_name=input("enter name ")
    last_name=input("enter  last name ")
    date_of_birth=input("enter birthdate ")
    e_mail=input("enter e_mail ")
    password=input("enter password ")
    DOB=datetime.datetime.strptime(date_of_birth,"%d/%m/%Y").date()
    print(DOB)
    valid_email= string_email_validation(e_mail)
    print(valid_email)
    validpass=valid_password(password)
    print(validpass)

def valid_password(password):
    l, u, p, d = 0, 0, 0, 0
    if (len(password) >= 8):
        for i in password:
    
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
    
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
    
            # counting digits
            if (i.isdigit()):
                d+=1           
    
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
       valid_password=password
       return valid_password
    else:
       raise Exception("invaid password")
    

def string_email_validation(s):
    at_index = s.find('@')
    dot_index = s.find('.')

    #check if there is no two consecutive dots or ats
    if(('@' and '.' in s) and s[at_index+1] != '@' and s[dot_index+1] != '.'):

        #domain name should be in allowed list
        if(s[-3:] in ('com','in','gov','edu','uk','org')):
            #can start with alphabets, numbers or certain special characters
            if(s[0].isalnum() or s[0] in ('-','_')):
                return s
            else:
                raise Exception("email not valid")
        else:
           raise Exception("email not valid")
    else:
       raise Exception("email not valid")
while True:
    print("1. register")
    print("2. login")
    print("3. exit")
    option=int(input("CHOOSE THE OPTION:"))
    if option==1:
        res=registered_detailed()
        print("registered_detailed",res)
    elif option==2:
        # res=user_login()
        # print("login users",res)
        pass
    elif option==3:
        break
    else:
        print("INVALID!")   