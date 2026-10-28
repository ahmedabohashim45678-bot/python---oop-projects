class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def printAll(self):
        print(self.name)
        print(self.age)
        print(self.gender)


class Employee(Person):
    def __init__(self, name, age, gender,salary):
        super().__init__(name, age, gender)
        self.salary=salary 


    def printAll(self):
            print(self.name)
            print(self.age)
            print(self.gender)
            print(self.salary)


class Manager:
    def __init__(self,name,id,loc):
          self.name=name
          self.id=id
          self.loc=loc

    def printAll(self):
            print(self.name)
            print(self.id)
            print(self.loc)



class Ceo(Employee,Manager):
    def __init__(self, name, age, gender, salary,id,loc):
          Employee.__init__(self,name,age,gender,salary)
          Manager.__init__(self,name,id,loc)


    def printAll(self):
            print(self.name)
            print(self.age)
            print(self.gender)
            print(self.salary)
            print(self.id)
            print(self.loc)


ceo1=Ceo("Mohamed",16,"Male",20000,"i1wi12","Egypt")
ceo1.printAll()
          
