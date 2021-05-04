def reverseDNA(x):
    data={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    trans=""
    for i in range(0,len(x)):
        y=str.upper(x[i])#to ensure that all letters are upper case
        trans=trans+str(data.get(y))
    return(trans)
x='aATgTc'
# an example, input your DNA sequence like this one
print(reverseDNA(x))#this will output the reverse complement
seq=input('DNA sequence:')#input your DNA sequence
print(reverseDNA(seq))#recall the function