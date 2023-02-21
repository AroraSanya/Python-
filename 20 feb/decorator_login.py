import datetime


student_data={}


def valid_password(min_length):
    def inner(func):
        def subinner(first_name,last_name,e_mail,passwd, *args, **kwargs):
            SpecialSym =['$', '@', '#', '%']
            val = True
            if len(passwd) < min_length:
                print('length should be at least 6')
                val = False
                
            if len(passwd) > 20:
                print('length should be not be greater than 8')
                val = False
                
            if not any(char.isdigit() for char in passwd):
                print('Password should have at least one numeral')
                val = False
                
            if not any(char.isupper() for char in passwd):
                print('Password should have at least one uppercase letter')
                val = False
                
            if not any(char.islower() for char in passwd):
                print('Password should have at least one lowercase letter')
                val = False

            if not any(char in SpecialSym for char in passwd):
                print('Password should have at least one of the symbols $@#')
                val = False
            if val:
                return val
            return func(first_name,last_name,e_mail,password, *args, **kwargs)
        return subinner
    return inner


def string_email_validation(func):
    def inner(first_name,last_name,s,*args,**kwargs):
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
        return func(first_name,last_name,s,*args,**kwargs)
    return inner 



@string_email_validation
@valid_password(min_length=6)
def registered_detailed(first_name,last_name,e_mail,password,date_of_birth):
    date=datetime.datetime.strptime(date_of_birth, "%d/%m/%Y").date()
    student_data["fname"]=first_name
    student_data["lname"]=last_name
    student_data["dob"]=date_of_birth
    student_data["email"]=e_mail
    student_data["password"]=password   

while True:
    print("1. register")
    print("2. login")
    print("3. exit")
    option=int(input("CHOOSE THE OPTION:"))
    if option==1:
        first_name=input("enter name ")
        last_name=input("enter  last name ")
        date_of_birth=input("enter birthdate ")
        e_mail=input("enter e_mail ")
        password=input("enter password ")
        res=registered_detailed(first_name,last_name,e_mail,password,date_of_birth)
        print("registered successfully")
        print(student_data)
    elif option==2:
        # res=user_login()
        # print("login users",res)
        pass
    elif option==3:
        break
    else:
        print("INVALID!")   