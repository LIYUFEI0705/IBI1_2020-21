
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
# open and get the elements of 'go_obo.xml'
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms= collection.getElementsByTagName("term")# get a list of elements called 'term'
is_a=collection.getElementsByTagName('is_a')# get a list of elements called is_a
id1=[]
id2=[]
id3=[]
id4=[]
is_alist=[]

for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    defstrtext=str(defstr.childNodes[0].data)
    id = term.getElementsByTagName('id')[0]
    idtext = str(id.childNodes[0].data)
    if 'DNA' in defstrtext:
        id1.append(idtext) #store gene id related to DNA
    if 'RNA' in defstrtext:
        id2.append(idtext)#store gene id related to RNA
    if 'protein'or 'Protein' in defstrtext:
        id3.append(idtext)#store gene id related to protein
    if 'carbohydrate'or 'Carbohydrate' in defstrtext:
        id4.append(idtext)#store gene id related to carbohydrate'''
'''for term in terms:
    id = term.getElementsByTagName('id')[0]
    idtext = str(id.childNodes[0].data)
    i = isa.childNodes[0].data
    b=is_a.index(i)
    if id1[i]==1:
        id1[idtext]=1
        for i in range(0,b):
            




a='GO:0000012'
print(func1(a))'''
l=1
#define a function to recursion the childnodes
def func1(a):
    x=[]
    global m
    m=[]
    m=a
    global count
    count=0
    for i in m:
        for isa in is_a:
            k=isa.childNodes[0].data
            if i==k:
                count+=1
                b=isa.parentNode
                idplace=b.getElementsByTagName('id')[0]
                idplace1=idplace.childNodes[0].data#get the id
                x.append(idplace1)# put it into a list
    m=x
    return m
while l==1:
    func1(id1)
    id1=m
    print(len(m))
    print((count))
    if count==0:
        break
























