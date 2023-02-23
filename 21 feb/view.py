from mvc_model import User,Blog
import csv
def get_all_user(user):
    # print("start")
    return user
def create_user(request):
    try:
        u1=User(request['first_name'],request['last_name'],request['e_mail'],request['mobile_no'])
        u1.set_user()
    except Exception as ee:
        raise Exception(ee)
    print("succses")


def create_blogs(request, user):
    b1 = Blog('dep', 'gjf', 'hfjf', user)
    b1.set_blog()
def get_user(users,id):
    for user in users:
        if user[0]==id:
            return user
        else:
            return "User not found"

