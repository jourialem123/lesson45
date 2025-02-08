#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them

class Student:
    name="Jouri"
    grade=10
    def display(self):
        print("I am a student")
    def intro(self):
        print("I am {} studying in grade {}".format(self.name,self.grade))   

st1=Student()       
st1.display()
st1.intro() 