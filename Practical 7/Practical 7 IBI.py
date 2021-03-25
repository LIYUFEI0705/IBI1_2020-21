import os
import pandas as pd # os allows us to work with files and directories, and pandas is for working with dataframes
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/admin/Desktop")# chdir()like cd
os.getcwd()#like pwd
os.listdir()#like ls
covid_data = pd.read_csv("full_data.csv")# we use the pandas library to read the content of the .csv file into a dataframeobject. We call our dataframe covid_data.
covid_data.head(5) # the fist line is signed as "0"( not include the title line) so it appears "0" to "4" lines of all columns
covid_data.head(6)# "0" to "5" lines, all columns
covid_data.info()# all data from the table
covid_data.describe()#  For each numeric column, this shows the number of entries, mean, SD and a number of quantiles(min,25%,50%,75%,max).
covid_data.iloc[0,1]# 仅此类型不包括标题行和编号列show the data in the first row(not include title line) and the second column(except 编号列）
covid_data.iloc[2,0:5]# 仅此类型不包括编号列list data in the third row and between the second column(编号列没有显示）to sixth column (title line will be shown as well)第三行05列的数据
covid_data.iloc[0:2,:]# 均包括0:2 mean that from the first（title row) to third rows, : mean that all columns (from 编号列 )
covid_data.iloc[0:10:2,0:5] # 均包括title line,0,2,4,6,8 rows；编号列 and next 5 columns
covid_data.iloc[0:3,[0,1,3]]# title line,0,1,2 row;编号列,0,1,3 columns
my_columns = [True, True, False, True, False, False]# 长度必须和表格中列的个数一样（包括编号列）
covid_data.iloc[0:3,my_columns]# show data in "True" columns, 编号列，0，2显示
covid_data.loc[2:4,"date"]# loc uses column names.第三行到第五行，“data"列的数据
data=[] # define a empty list
for i in range(0,7996):# to choose covid_data.iloc[i,1]== "Afghanistan" 的数据
	if covid_data.iloc[i,1]== "Afghanistan":
		data.append(True)
	else:
		data.append(False)
covid_data.loc[data,"location"]  # 显示”locaion“列 covid_data.iloc[i,1]== "Afghanistan"的数据


worlddata=[]
for i in range(0,7996):# to choose covid_data.iloc[i,1]== "World" 的数据
	if covid_data.iloc[i,1]== "World":
		worlddata.append(True)
	else:
		worlddata.append(False)
covid_data.iloc[worlddata,[0,2]]
world_new_cases=covid_data.iloc[worlddata,2]# put the "new cases" column into new dataframe world_new_cases
world_dates=covid_data.iloc[worlddata,0]#put the "date" column
world_new_death=covid_data.loc[worlddata,"new_deaths"]
plt.boxplot(world_new_cases)# make a boxplot
plt.show()
print(world_new_cases.mean())#calculate the mean of worldwide new cases
print(world_new_cases.median())#calculate the median od worldwide new cases
plt.plot(world_dates, world_new_cases, 'b+',world_dates,world_new_death,'co')# scatter gragh, 用蓝色的×表示
# r+就是红色的×，bo就是蓝色的圆点表示
#the following learnt from https://www.jb51.net/article/184860.htm
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()

China_data=[]
for i in range(0,7996):# to choose covid_data.iloc[i,1]== "China" 的数据
	if covid_data.iloc[i,1]== "China":
		China_data.append(True)
	else:
		China_data.append(False)
China_new_cases=covid_data.loc[China_data,"new_cases"]
China_dates=covid_data.loc[China_data,"date"]
China_total_deaths=covid_data.loc[China_data,"total_deaths"]
China_total_cases=covid_data.loc[China_data,"total_cases"]
print("the proportion of cases have died in China is ", China_total_deaths.sum()/China_total_cases.sum())

UK_data=[]
for i in range(0,7996):# to choose covid_data.iloc[i,1]== "United Kingdom" 的数据
	if covid_data.iloc[i,1]== "United Kingdom":
		UK_data.append(True)
	else:
		UK_data.append(False)
UK_new_cases=covid_data.loc[UK_data,"new_cases"]
UK_dates=covid_data.loc[UK_data,"date"]
UK_total_deaths=covid_data.loc[UK_data,"total_deaths"]
UK_total_cases=covid_data.loc[UK_data,"total_cases"]
print("the proportion of cases have died in the UK is ", UK_total_deaths.sum()/UK_total_cases.sum())
plt.plot(UK_dates,UK_new_cases,'bo',China_dates,China_new_cases,'m+')# we put two kinds of data into a figure(use"comma" to seperate)
plt.show()
#'b' 蓝色 'm' 洋红色 magenta
#'g' 绿色 'y' 黄色
#'r' 红色 'k' 黑色
#'w' 白色 'c' 青绿色 cyan
#'#008000' RGB某颜色 '0.8' 灰度值字符串
#多条曲线不指定颜色时，会自动选择不同颜色
#链learnt from ：https://www.jianshu.com/p/ed3f31fc6a41

