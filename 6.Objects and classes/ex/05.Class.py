class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.count = 0

    def add_student(self, name, grade):
        if self.count < Class.__students_count:
            self.count += 1
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(float(grade) for grade in self.grades) / self.count

    def __repr__(self):
        result = ""
        result += f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"
        return result

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
