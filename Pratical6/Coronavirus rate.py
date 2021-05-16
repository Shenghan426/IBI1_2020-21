import matplotlib.pyplot as plt #import the python package
labels ='USA','India','Brazil','Russia','UK' #list the name of each data
sizes =[29862124,11285561,11205972,4360823,4234924] #list the data
explode =(0.1,0,0,0,0,) # make the USA data exploded
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal') #ensure it is a circle
plt.title("Coronavirus Infection Rates across Countries") #set the title
plt.show()