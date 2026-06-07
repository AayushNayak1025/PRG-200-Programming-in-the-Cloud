# Student Report Card System
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()

        if avg >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print("Name:", self.name)
        print("Average:", round(avg, 2))
        print("Grade:", self.grade())
        print("Result:", result)
        print()


students = [
    ("Sampanna", [78, 85, 60, 90, 72]),
    ("Nikhil", [45, 50, 38, 60, 55]),
    ("Amrit", [30, 25, 40, 35, 28]),
    ("Prashant", [90, 88, 95, 92, 87]),
]

student_objects = []

for name, marks in students:
    student_objects.append(Student(name, marks))

for student in student_objects:
    student.display()