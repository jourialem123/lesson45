class Parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        print("{} is singing a {} song".format(self.name,song))   
    def dance(self):
        print("{} is dancing".format(self.name))    

p1=Parrot("Rio",3)
p2=Parrot("Blu",2)

print("This parrot's species is {}, its name is {} and it is {} years old ".format(p1.species,p1.name,p1.age))
print("This parrot's species is {}, its name is {} and it is {} years old ".format(p2.species,p2.name,p2.age)) 

p1.sing("happy")       
p1.dance()
p2.sing("party")
p2.dance()