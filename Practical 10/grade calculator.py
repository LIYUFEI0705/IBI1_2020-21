def grade(name,code,poster,final):#'name' is the student name, 'post' is the grade for poster presentation,'final' is the grade for final exam
    totalgrade=0
    totalgrade=float(code)*0.4+float(poster)*0.3+float(final)*0.3
    # calculate your final grade
    final=name+' Your final grade is:'+str(totalgrade)
    return final
grade('wz',98,98,98)#an example to recall the function,'wz'is the student name,
# input your name and scores for every task when running
# for example: when running, it will show
#Student Name:
#Grade for code portfolio:
#Grade for poster presentation:
#Grade for final exam:
#and then you can write in the running terminal to input your data
#finally it will output the answer
a=input('Student Name:')
b=input('Grade for code portfolio:')
c=input('Grade for poster presentation:')
d=input('Grade for final exam:')
print(grade(a,b,c,d))
