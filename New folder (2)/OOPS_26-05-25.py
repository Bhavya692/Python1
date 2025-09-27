'''class students():
    location='TN'
    course='PFS'
bhavya=students()
Divya=students()
Amir=students()
#accessing class variables using obj reference
print(bhavya.location,bhavya.course)
print(Divya.location,Divya.course)
print(Amir.location,Amir.course)
print('-------------------------')
#accessing class variables using class reference
print(students.location,students.course)
print('-------------------------')
#modifying class variable using obj reference
bhavya.course='JFS'
print(bhavya.location,bhavya.course)
print(Divya.location,Divya.course)
print(Amir.location,Amir.course)
#modifying class variable using class reference
students.course='JFS'
print(bhavya.location,bhavya.course)
print(Divya.location,Divya.course)
print(Amir.location,Amir.course)

class sample():
    a=10
    def __init__(self):
        print('Hello')
        print(self)
obj1=sample()
print(obj1)
obj2=sample()
print(obj2)

class sample():
    a=10
    def __init__(self):
        print('Hello')
        print(f'self={self}')
obj1=sample()
print(obj1)
obj2=sample()
print(obj2)'''

class students():
    def __init__(self,name,mobno,email_id):
        self.name=name
        self.mobno=mobno
        self.email_id=email_id
obj1=students('pushpa',999999999,'brand@gmail.com')
obj2=students('virat',9181818181,'king@gmail.com')
obj3=students('srivalli',8888888888,'srivalli@gmail.com')
#accessing obj variable by using obj reference
print(obj1.name,obj1.mobno,obj1.email_id)
print(obj2.name,obj2.mobno,obj2.email_id)
print(obj3.name,obj3.mobno,obj3.email_id)
print('------------------------')
#modifying obj variables by using obj ref
obj1.email_id='pushparaj@gmail.com'
print(obj1.name,obj1.mobno,obj1.email_id)
print(obj2.name,obj2.mobno,obj2.email_id)












