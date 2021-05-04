class Student(object):# define a class called'Student
    def __init__(self,x,y,z):
        self.firstname=x
        self.familyname=y
        self.undergraduate=z
    def add(self):# a funtion to print full name and undergraduate programme in a line
        n=self.firstname+' '+self.familyname+' '+self.undergraduate
        print(n)
example=Student('Sehun','Oh','BMS')
#an example, input your example as (given name,family name, undergraduate programme)
example.add()# to reacll the function in this class
a=input('Your given name:')
b=input('Your family name:')
c=input('Your undergraduate programme: ')
student=Student(a,b,c)#to make the'student' to be the 'Student'class
student.add()#recall add() function in the class
