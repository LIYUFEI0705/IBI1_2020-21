DIC={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'USA', 'India', 'Brazil', 'Russia','UK'#give every part a name
sizes = [29862124, 11285561, 11205972, 4360823,4234924]# the data distributed in pie chart
explode = (0,0,0,0,0)  # Set each item n radii from the center of the circle

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)#draw a pie chart
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('The proportion of COVID-19 infections from 5 countries')
plt.show()#show the pie chart
#we use the example of pie chart from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py
#and use the data from our practical
#comment on this task: I have known a lot of settings of the pi chart and the code is easy to run
# make a frequency table
plt.bar(labels,sizes)
plt.title('The proportion of COVID-19 infections from 5 countries')
plt.show()
