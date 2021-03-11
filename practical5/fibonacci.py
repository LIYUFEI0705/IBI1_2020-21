# we want to output 1,1,2,3,5,8,......
#so we need to replace a or b with a+b
# the first line to the third line are to define a,b,c
#the fourth line to the sixth line are to loop
# if we write a,b=b,a+b in two lines,the it will output 1,2,4,8,......
a=1
b=1
i=1
for i in range(1,14):
    print(a)
    a,b=b,a+b

