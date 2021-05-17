import os
import pandas as pd # os allows us to work with files and directories, and pandas is for working with dataframes
import matplotlib.pyplot as plt
import numpy as np
#os.chdir("C:/Users/admin/Desktop")# command chdir()like cd in Unix
covid_data = pd.read_csv("full_data.csv")# we use the pandas library to read the content of the .csv file into a dataframeobject. We call our dataframe covid_data.
print(covid_data.iloc[0:11:2,:])
new_cases=covid_data.loc[:,"new_cases"]

# successfully use a Boolean to show “total cases” for all rows corresponding to Afghanistan
data=[] # define a empty list
for i in range(0,7996):# to choose data in covid_data, with "location" showing "Afghanistan"
        if covid_data.iloc[i,1]== "Afghanistan":
                data.append(True)
        else:
                data.append(False)# creat a Boolean list
print(covid_data.loc[data,"total_cases"]) # show ”total_cases“column of data in Afghanistan

#correctly compute the mean and median of new cases for the entire world.
#successfully create a boxplot of new cases worldwide.
#successfully plot both new cases and new deaths worldwide.
worlddata=[]
for i in range(0,7996):# to choose data in covid_data, with "location" showing "World" 
	if covid_data.iloc[i,1]== "World":
		worlddata.append(True)
	else:
		worlddata.append(False)
world_new_cases=covid_data.iloc[worlddata,2]# put the "new cases" column into new dataframe world_new_cases
print('the mean of worldwide new cases is:',world_new_cases.mean())#calculate the mean of worldwide new cases
print('the median of worldwide new cases is:',world_new_cases.median())#calculate the median od worldwide new cases
plt.boxplot(world_new_cases)# make a boxplot
plt.ylabel("number")
plt.xlabel(" new cases worldwide")
plt.title( " the distribution of new cases of Covid-19 worldwide")
plt.show()
world_new_death=covid_data.loc[worlddata,"new_deaths"]
world_dates=covid_data.iloc[worlddata,0]
plt.plot(world_dates, world_new_cases, 'b+',label='new cases')
plt.plot(world_dates,world_new_death,'c+',label=('new death'))
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
# makes the x-axis labels rotate 90 degrees counterclockwise
# Tweak spacing to prevent clipping of tick-labels
plt.xlabel("date")
plt.ylabel("number")
plt.title(" new cases and new deaths of Covid-19 worldwide")
plt.legend()
plt.show()


# The following commands answer the question in question.txt
China_data=[]
for i in range(0,7996):# to choose data in covid_data, with "location" showing "China"
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
for i in range(0,7996):# to choose data in covid_data, with "location" showing "United Kingdom"
	if covid_data.iloc[i,1]== "United Kingdom":
		UK_data.append(True)
	else:
		UK_data.append(False)
UK_new_cases=covid_data.loc[UK_data,"new_cases"]# use new list to store data we want
UK_dates=covid_data.loc[UK_data,"date"]
UK_total_deaths=covid_data.loc[UK_data,"total_deaths"]
UK_total_cases=covid_data.loc[UK_data,"total_cases"]
print("the proportion of cases have died in the UK is ", UK_total_deaths.sum()/UK_total_cases.sum())

#plot new cases in China and the UK
plt.plot(China_dates, China_new_cases, 'b+',label=('China'))
plt.plot(UK_dates,UK_new_cases,'c+',label=('the UK'))
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
# makes the x-axis labels rotate 90 degrees counterclockwise
#the following commands learnt from :https://www.jb51.net/article/184860.htm
# Tweak spacing to prevent clipping of tick-labels
plt.xlabel("date")
plt.ylabel("number")
plt.title(" new cases and new deaths of Covid-19 in China and the UK")
plt.legend()
plt.show()
