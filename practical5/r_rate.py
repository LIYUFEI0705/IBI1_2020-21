# remember r is the people that will be infected, don not forget to add the ori$
# range(a,b)is to produce a number between a and b-1
n=84
r=1.5
i=1
for i in range(1,6):
    n=n*(r+1)

print("Every patient can infects average",str(r),'normal individuals.When there are',str(int(n)),'individuals infected after 5 generations')


