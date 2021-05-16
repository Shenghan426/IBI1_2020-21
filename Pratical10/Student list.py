
class Student: # create a class called student
    def __init__(self, first_name, last_name, majority): # define init
        self.first_name = first_name
        self.last_name = last_name
        self.undergraduate_programme = majority

    def output(self): # define a function to print the information
        print("Student's name is "+self.first_name +" "+
              self.last_name+ ", whose majority is "+self.undergraduate_programme)
#example
student1=Student('Tony','Fei','BMS')
student1.output()



