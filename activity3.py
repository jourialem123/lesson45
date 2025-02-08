#Write a program to create a class Parrot and perform the following tasks -
#  Create a class variable species 
# Create a __init__ method that has instance variables - name and age 
# Create instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well

class Parrot:
    species="Parrot"

    def __init__(self,name,age):
       self.name=name
       self.age=age

p1=Parrot("Rio",3)
p2=Parrot("Blu",2)

print("This parrot's species is {}, its name is {} and it is {} years old ".format(p1.species,p1.name,p1.age))
print("This parrot's species is {}, its name is {} and it is {} years old ".format(p2.species,p2.name,p2.age))
