a=050702
b=190784
c=100321
d=abs(c-a)
e=abs(b-a)
if d>=e:
    print(" d is bigger than e")
elif d<e:
    print("d is smaller than e")
y=False
x=True
z=(x and not y)or(y and not x)
print(z)
w=(x!=y)
print(w)
print(z==w)
