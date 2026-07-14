class Calculator:
    def sum(self, *args):
        return sum(args)

c = Calculator()
val =c.sum(5,10,20,30)
print(val)
print("-------------------------")

class Profile:
    def show_info(self,**kwargs):
        for key,value in kwargs.items():
            print(f"{key} : {value}")

u = Profile()
u.show_info(name="David",age=30,role="administrator")

class Student:
    def student_info(self,*args,**kwargs):
        print(args)
        print(kwargs)

c = Student()
c.student_info("a","b","c",name="David",age=30,role="administrator")