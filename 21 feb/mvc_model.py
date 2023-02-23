import uuid
import csv

c_data =[]
blog_data=[]
data =[]
student_data={}
blog ={}
def generate_uuid():
    id = uuid.uuid4()
    return str(id)
class User(object):
    def __init__(self, first_name, last_name, e_mail, mobile_no):
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.mobile_no = mobile_no
        self.uuid = generate_uuid()
    def set_user(self):
        student_data['id'] = self.uuid
        student_data["fname"]=self.first_name
        student_data["lname"]=self.last_name
        student_data["email"]=self.e_mail
        student_data["mobile_no"]=self.mobile_no
        with open('user.csv', "a+" , newline='') as file:
                writer = csv.writer(file)
                data =[student_data['id'],
                       student_data['fname'],
                       student_data['lname'],
                       student_data['email'],
                       student_data['mobile_no']]
                writer.writerow(data)
                file.close()
    def intials(self):
        return self.first_name + "."+ self.last_name
    @classmethod
    def getallUser(self):
         with open('user.csv', 'r')as fp:
            data = csv.reader(fp)
            return list(data)
class Blog(object):
    def __init__(self, title , body , create_date, user):
        self.user = user
        self.title = title
        self.body = body
        self.create_date = create_date
    def set_blog(self):
        blog['user'] = self.user
        blog['title'] = self.title
        blog['body'] = self.body
        blog['create_date'] = self.create_date
        blog['id'] = generate_uuid()
        with open('blog.csv', "a+" , newline='') as file:
                writer = csv.writer(file)
                data =[blog['user'],
                        blog['title'],
                        blog['body'] ,
                        blog['create_date'],
                        blog['id']]
                writer.writerow(data)
                file.close()
    @classmethod
    def get_all_blogs(self):
        with open('blogs.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        blog_data.append(blog)
class Comments(object):
    def _init_(self, comment , blog ,  user):
        self.user = user
        self.blog = blog
        self.comment = comment
    def set_comment(self):
        blog['user'] = self.user
        blog['blog'] = self.blog._dict_
        blog['comment'] = self.comment
        blog['id'] = generate_uuid()
        with open('comment.csv', "w") as file:
             c_data.append(blog)
u1 = User('Sanya', 'Arora','Sanya@gmail.com', '938499455')
u1.set_user()
b1 = Blog('dep', 'gjf', 'hfjf', u1)
b1.set_blog()
# b1.get_all_blogs()