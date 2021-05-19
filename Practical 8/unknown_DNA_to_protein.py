import os
import pandas as pd
import re
import linecache as ls
#find the way the file download
#os.chdir("C:/Users/admin/Desktop")
fhand=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
count=0#count the total number of lines in fhand
startplace=[]#set the startplace of every unknown function 
endplace=[]#set the endplace of every unknown function 
mrnaname=[]#record the name of every unknown
rna=""
number=0#record the number of unknown mRNA
a=False
for line in fhand:
    count=count+1
    if 'unknown function' in line:
        x=re.findall(r'^>(\S+)_',line)
        mrnaname.append(x)
        startplace.append(count+1)
        number=number+1
        if a==True:
            endplace.append(count)
        a=True# mark the finding of startplace
    elif (line[0]=='>'and a==True)or count==156008 :# judge when the endplace should be recorded
        endplace.append(count)
        a=False#mark one DNA has been extracted           

#a self-defined function to extract DNA slices
def extract(a,b):
    rna=""
    for i in range(a,b):
       rna=rna+str(ls.getline('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa',i).strip())
    return rna
AAcode={'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L', 'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'CCT':'P', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'ATT':'I', 'ATC':'I', 'ATA':'J', 'ATG':'M', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V', 'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'TAT':'Y', 'TAC':'Y', 'TAA':'O', 'TAG':'U', 'TGT':'C', 'TGC':'C', 'TGA':'X', 'TGG':'W', 'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Z', 'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AAT':'N', 'AAC':'B', 'AAA':'K', 'AAG':'K', 'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
#a self-defined function to translate DNA slices
def translate(x):
    output=""
    for i in range(1,len(x),3):
        a=x[i-1:i+2]
        b=AAcode[str(a)]
        output=output+b
    return output
code=[]#record the protein slices in a list
protein_length=[]#record the length of every protein slice in a list
for i in range(0,number):
    z=extract(startplace[i],endplace[i])
    y=translate(z)
    x=len(str(y))
    code.append(y) 
    protein_length.append(x)
#create a new fasta file and write it
filename=str(input('input a file name end with .fa:'))
simplify=open(filename,'w')
for i in range(1,2*number+1):# write in the new file
    if i%2==1:
        linei=str(mrnaname[int((i-1)/2)])+str(protein_length[int((i-1)/2)])
        simplify.write(linei)
        simplify.write('\n')
    else:
        linei=str(code[int(i/2-1)])
        simplify.write(linei)
        simplify.write('\n')
simplify.close()

    

    
