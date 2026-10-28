from abc import ABC,abstractmethod
class Student(ABC):
    @abstractmethod
    def check_grade(self):
        pass
class GradeEvaluator(Student):
    def __init__(self,grade):
        self.grade=grade
    def check_grade(self):
        if  self.grade >=90:
            print("Excellent")
        elif self.grade >=75:
            print("Good")
        else:
            print("Needs Improvement")
B3=GradeEvaluator(80)
B3.check_grade()
B3=GradeEvaluator(120)
B3.check_grade()
B3=GradeEvaluator(50)
B3.check_grade()
