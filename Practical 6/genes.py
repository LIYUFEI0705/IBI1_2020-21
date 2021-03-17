import numpy as np
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
a=np.array(gene_lengths)# use the functions in numpy to create an array
b=np.array(exon_counts)
average_exonlengths=a/b
average_exonlengths.sort()#use sort() to sort data
import matplotlib.pyplot as plt
plt.boxplot(average_exonlengths)
# use data in average_exonlengths to create a boxplot
plt.ylabel("average exon lengths")#define the y axis in boxplot
plt.xlabel("different genes")#define the x axis in boxpl
plt.title('The distribution of the average exon lengths of 10 different genes')
plt.boxplot(average_exonlengths,notch=False,medianprops={'color':'red'},boxprops=dict(color="blue"), whiskerprops = {'color': "black"},capprops = {'color': "cyan"},flierprops={'color':'purple','markeredgecolor':"purple"})
#change the color
plt.show()#show the boxplot
  
