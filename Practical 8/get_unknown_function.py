import os
import pandas as pd
import re
import linecache as ls
#os.chdir("C:/Users/admin/Desktop")#import the palce where the file exist
fhand=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
count=0
startplace=[]
endplace=[]
mrnaname=[]
rna=""
number=0#record the number of unknown function RNA
a=False
for line in fhand:#record the startplace and endplace of every unknown function DNA
    count=count+1
    if 'unknown function' in line:
        x=re.findall(r'^>(\S+)_',line)
        mrnaname.append(x)
        startplace.append(count+1)
        number=number+1
        if a==True:
            endplace.append(count)
        a=True
    elif (line[0]=='>'and a==True)or count==156008 :
        endplace.append(count)
        a=False           

def extract(a,b):# a self-defined function to extract RNA
    rna=""
    for i in range(a,b):
       rna=rna+str(ls.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',i).strip())
    return rna
gene_code=[]
mrna_length=[]
# record the length of every unknown function RNA and slices of every unknown RNA 
for i in range(0,number):
    z=extract(startplace[i],endplace[i])
    x=len(str(z))
    gene_code.append(z) 
    mrna_length.append(x)
simplify=open('unknown_function.fa','w')#make a new file to store the data
for i in range(1,2*number+1):
    if i%2==1:
        linei=str(mrnaname[int((i-1)/2)])+str(mrna_length[int((i-1)/2)])
        simplify.write(linei)
    else:
        linei=str(gene_code[int(i/2-1)])
        simplify.write(linei)
simplify.close()

