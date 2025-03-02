class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__people_list = list()
        
    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__people_list:
            person.describe()
    
    def addPerson(self, person):
        self.__people_list.append(person)
        
    
    def countPerson(self, Person):
        count = 0
        for person in self.__people_list:
            if isinstance(person, Person):
                count += 1
        return count
    
    def sortAge(self):
        self.__people_list.sort(key=lambda x: x._yob)
        
    def avgYob(self, Person):
        sum = 0
        for person in self.__people_list:
            if isinstance(person, Person):
                sum += person._yob
        return sum / self.countPerson(Person)
  
  
from abc import ABC, abstractmethod          
class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name 
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: int):
        super().__init__(name, yob)
        self.__grade = grade  

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")  


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialization: str):
        super().__init__(name, yob)
        self.__specialization = specialization

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialization: {self.__specialization}")

student1 = Student ( name ="studentA ", yob =2010 , grade ="7")
student1 . describe ()


teacher1 = Teacher (name ="teacherA ", yob =1969 , subject ="Math")
teacher1 . describe ()

doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialization ="Endocrinologists ")
doctor1 . describe ()

print()
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialization =" Cardiologists ")
ward1 = Ward (name ="Ward1")
ward1.addPerson( student1 )
ward1.addPerson( teacher1 )
ward1.addPerson( teacher2 )
ward1.addPerson( doctor1 )
ward1.addPerson( doctor2 )
ward1.describe()

print()
print(f"Number of doctors in ward1: {ward1.countPerson(Doctor)}")
print(f"Number of teachers in ward1: {ward1.countPerson(Teacher)}")
print(f"Number of students in ward1: {ward1.countPerson(Student)}")

print()
print ("After sorting Age of Ward1 people: ")
ward1.sortAge()
ward1.describe()

print()
print(f"Average YoB of students in ward1: {ward1.avgYob(Student)}")
print(f"Average YoB of teachers in ward1: {ward1.avgYob(Teacher)}")
print(f"Average YoB of doctors in ward1: {ward1.avgYob(Doctor)}")

