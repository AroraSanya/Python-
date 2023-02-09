users=[]
dict={}
dict["subjects"]=[]

def list_of_students(users):
    return users

def search_students(users):
    name = input("Enter the name: ")
    for i in users:
        if i['name'] == name:
            user = i
        else:
            user = "Invalid Name"
    return user
def update_student():
    roll_no = int(input("Enter the Roll number:"))
    name = input("Enter the name: ")
    subject = input("Enter the subject:")
    Class = input("Enter the class:")
    for i in users:
        if i['roll_no'] == roll_no:
            dict['name'] =  name
            dict['subject'].append(subject)
            dict['class'] =  Class

def delete_student(users):
    roll_no = int(input("Enter the roll number:"))
    for i in users:
        if i['roll_no'] == roll_no:
            users.remove(i)



def add_student():
    roll_no = int(input("Enter the Roll number:"))
    name = input("Enter the name: ")
    subject = input("Enter the subject:")
    Class = input("Enter the class:")

    dict['roll_no'] =roll_no
    dict['name']=name
    dict['subjects'].append(subject)
    dict['class'] = Class

    users.append(dict)
    return dict

while True:
    print("1. LIST THE STUDENTS")
    print("2. SEARCH THE STUDENTS")
    print("3. UPDATE STUDENTS")
    print("4. DELETE THE  STUDENTS")
    print("5. ADD THE STUDENTS")
    print("6. EXIT")

    option=int(input("CHOOSE THE OPTION:"))
    if option==1:
        res=list_of_students(users)
        print(" list of students",res)
    elif option==2:
        res=search_students(users)
    elif option==3:
        res=update_student()
        print(res)
    elif option==5:
        res=add_student()
        print("added succesfully")
    elif option==6:
        break    
    else:
        print("INVALID")
        
    
        
    





