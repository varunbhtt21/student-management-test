class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} added to {self.subject} class")

    def display(self):
        print(f"\nTeacher: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"Students: {len(self.students)}")
