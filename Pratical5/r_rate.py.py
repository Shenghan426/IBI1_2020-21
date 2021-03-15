#the initial infected number
n=84
# the r rate
r=1.1
# loop for five times
for i in range(1,6):
    n=n*r+n #the number of each times of infection 
print (n) #the final number

