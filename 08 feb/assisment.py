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

# string_email_validation(s)
# def password_checker(password):
#     flag = 0
# @Registration_format
# def user_login(email_id,password):
#     return email_id
#     return password
#     while True:
#         if(Registration_format(email_address)==user_login(email_id)):
#             elif (Registration_format(password_checker)==user_login(password)):
        
# while True:
#     if len(password)<=8:
#         flag = -1
#         print("enter the password having minimum length 8")
#         break
#     elif not re.search("[a-z]",password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]" , password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         return "Valid Password"
#         break
#     if flag == -1:
#     return "not a valid password"
# message= input("enter the details")
# user_first_name = input("enter the first name =")
# user_last_name = input("enter the last name =")
# user_birthday = input('Enter your birthday in dd/mm/yyyy format')
# day, month, year = list(map(int, user_birthday.split("/")))
# birthdate = datetime.date(year,month,day)
# a = Registration_format(user_first_name,user_last_name,user_birthday)

# print("first_name = ",user_first_name)
# print("last_name = ",user_last_name)
# print("birthday = ", user_birthday)
# email_enter = input("enter email address =")
# b = email_address(email_enter)
# print("email_address = ",b)
# password_enter = input("enter the password=")
# c1 = password_checker(password_enter)
# print(c1)
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
        print("INVALID")    