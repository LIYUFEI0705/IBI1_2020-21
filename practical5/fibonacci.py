# we want to output 1,1,2,3,5,8,......
#so we need to replace a or be with a+b
a=1
b=1
i=1
for i in range(1,14):
    print(a)
    a,b=b,a+b
    
