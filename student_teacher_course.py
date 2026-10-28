class Person:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def introduce(self):
            print(self.name)
            print(self.age)
            print(self.id)
    def show_id():
        pass 
class Student(Person):
    def __init__(self,name,age,id,grade,courses_enrolled):
        super().__init__(name,age,id)
        self.grade=grade
        self.courses_enrolled=courses_enrolled
    def enroll(self,course):
        self.courses_enrolled.append(course)
class Teacher(Person):
    def __init__(self,name,age,id,subject,salary):
        super().__init__(name,age,id)
        self.subject=subject
        self.salary=salary
        self.assigned_students=[]
    def assign_grade(self,student,grade):
        self.assigned_students.append((student,grade))
B3=Student("Ahmed",16,"B3rrdy","B3",["Programming"])
B3.enroll("AI")  
print(B3.courses_enrolled)
df=Student("Ahmed",16,"B3rrdy","B3",["Programming"])
df.enroll("Math")    
T1=Teacher("Ahmed",16,"B3rrdy","English",1000)
T1.assign_grade("Ahmed","A")
T1=Teacher("Ahmed",16,"B3rrdy","English",1000)
T1.assign_grade("B3","B+")
