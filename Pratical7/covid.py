#import packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:/world health/") #change working directory
covid_data = pd.read_csv("full_data.csv") #import the dataset
print(covid_data.iloc[0:11:2, 0:5]) # print the every second row between (and including) 0 and 10
def country_list(country):#define a function to use the boolean to find the result
    country_booleans = []#the boolean function
    for row in covid_data.iloc[0:7996,1]:
        if row == country:
            country_booleans.append(True)
        else:
            country_booleans.append(False)
    return country_booleans
afg_list = country_list("Afghanistan") #give the condition
print(covid_data.loc[afg_list,"total_cases"])#print the result
world= [] # use the "for loops" to find rows which are about "world".
for a in range (0,7996):
     if covid_data.iloc[a,1] == "World":
        world.append(a)
world_new_cases = covid_data.loc[world,"new_cases"]
world_dates = covid_data.loc[world,"date"]
mean=np.mean(world_new_cases)# use the numpy to compute the mean
median=np.median(world_new_cases)# use the numpy to compute the median
print(mean)#print the mean
print(median) # print the median
plt.plot(world_dates, world_new_cases, "b+")
plt.title("New cases of the world")#set the title
plt.xticks(world_dates.iloc[0:len(world_dates):5], rotation=-90)#set the x axis
plt.show() # make a plot of the new case of the world
plt.boxplot(world_new_cases, showfliers = False, labels = ["Boxplot of new cases of the world"])
plt.show() # make a boxplot
#Q:How have new cases and total cases developed over time in Spain?
spain_boolean=country_list("Spain") #use the function again to list the data of Spain
Spain_new_cases=covid_data.loc[spain_boolean, "new_cases"]
Spain_dates = covid_data.loc[spain_boolean, "date"]
Spain_total_cases = covid_data.loc[spain_boolean, "total_cases"]
plt.plot(Spain_dates, Spain_new_cases, "b+")#show the plot of the Spain new cases
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):5], rotation=-90)# set the x axis
plt.title("New cases in Spain ")#set the title
plt.show()
plt.plot(Spain_dates, Spain_total_cases, "b+")# show the plt of the Spain total cases
plt.title("Total cases in Spain ")#set the title
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):5], rotation=-90)#set the x axis
plt.show()