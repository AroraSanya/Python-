from mvc_model import User
import view
def showallUser():
    users=User.getallUser()
    return view.get_all_user(users)
def request():
    requests={}
    print("To create the user,input your data:")
    requests['first_name']= input("enter your first name:")
    requests['last_name']= input("enter your last name:")
    requests['e_mail']= input("enter your email-id:")
    requests['mobile_no']= input("enter your mobile no.:")
    return view.create_user(requests)
def delete_user():
    id=input("enter id  you want to delete")
def request_blog():
    request={}
    # request['user']  = input("Enter the user id")
    request['title']  = input("Enteer the title: ")
    request['body']  = input("Enteer the body: ")
    request['create_date']  = input("Enteer the creat date : ")
    # request.get_one_user()
    new_var=get_one_user()
    print(new_var)
    return view.create_blogs(request,new_var)


def get_one_user():
    id=input("enter the unique id")
    users=User.getallUser()
    # print(users)
    return view.get_user(users,id)
        
        # print(type(user['id']))

    
# user_id()    
request_blog()
print(get_one_user())

# print(showallUser())