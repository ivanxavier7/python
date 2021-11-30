class Student:
    #Special methods
    def __init__(self, name, age):     # Construtor do objeto
        self.name = name
        self.age = age
        self.grades = (90, 80, 93, 78, 90)
    # Altera no output para o user
    def __str__(self):
        return f"Nome: {self.name} Age: {self.age}"
    # Altera tambem n o debugger
    def __repr__(self):
        return f"<Person: {self.name}, {self.age})>"
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Ivan", 27)
student2 = Student("Vasco", 26)
print(student.name)
print(student.grades)
print(Student.average(student))
print(student.average())

print(student)
print(student2)
