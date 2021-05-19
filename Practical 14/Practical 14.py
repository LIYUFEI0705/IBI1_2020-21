
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
# open and get the elements of 'go_obo.xml'
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")# get a list of elements called 'term'

dict={}
# use a dictionary called 'dict' to contain all childnodes
for term in terms:
    idtext = term.getElementsByTagName('id')[0].childNodes[0].data#get the text of id in every term
    dict[idtext]=[]# to prepare to fill the childnodes for each term
for term in terms:
    id=term.getElementsByTagName('id')
    is_a=term.getElementsByTagName('is_a')
    for isa in is_a:
        dict[isa.firstChild.data].append(id[0].firstChild.data)# fill the childnodes of each id

def count2(counter):# the function to count the childnodes
    for i in counter:
        if i not in list:
            list.append(i)# to add new childnodes in list
            count2(dict[i])# to recursion
    return len(list)

def count(x):# the function used to see whether the id is related to x and to calculate the childnodes number
    global list
    for term in terms:
        defstr=term.getElementsByTagName('defstr')[0].firstChild.data
        ids = term.getElementsByTagName('id')[0].childNodes[0].data  # get the id information
        if x in defstr:# to see whether this id is a x-related gene
            if dict[ids]!= 0:# see whether there are childnodes
                n=count2(dict[ids])
    return n

list=[]# make the list blank before recall the function
nDNAs=count('DNA')
print('the number of childnodes of RNA is:',str(nDNAs))
list=[]
nRNAs=count('RNA')
print('the number of childnodes of DNA is:',str(nRNAs))
list=[]
protein1=count('Protein')
list=[]
protein2=count('protein')
nproteins=protein2+protein1
print('the total childnodes number of protein is:',str(nproteins))
list=[]
oligosaccharide1=count('oligosaccharide')
list=[]
oligosaccharide2=count('Oligosaccharide')
noligosaccharides=oligosaccharide2+oligosaccharide1
print('the total childnodes number of oligosaccharide is:',str(noligosaccharides))

sizes=[nDNAs,nRNAs,nproteins,noligosaccharides]
labels = [u'RNA',u'DNA',u'protein',u'oligosaccharide']
explode = (0.05,0,0,0.05)
plt.title('The number of Childnodes of DNA,RNA,Protein,oligosaccharide')
patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
plt.axis('equal')
plt.legend()
plt.show()












