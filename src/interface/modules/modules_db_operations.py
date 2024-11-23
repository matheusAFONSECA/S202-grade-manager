class ModulesDBoperations:
    def __init__(self, db, student, teacher, subject, grade):
        self.db = db
        self.student = student
        self.teacher = teacher
        self.subject = subject
        self.grade = grade

    def create_base_data(self):
        # Criando estudantes
        students = [
            self.student(1, "Computer Science", "Matheus Fonseca", self.db),
            self.student(2, "Computer Science", "Alvaro Lucio", self.db),
            self.student(3, "Computer Science", "Thiago Rocha", self.db),
            self.student(4, "Computer Science", "Pedro Luis", self.db),
        ]
        for student in students:
            student.create_student()

        # Criando professores
        teachers = [
            self.teacher(101, "Yvo", self.db),
            self.teacher(102, "Renzo", self.db),
            self.teacher(103, "Chris", self.db),
            self.teacher(104, "Ewel", self.db),
        ]
        for teacher in teachers:
            teacher.create_teacher()

        # Criando matérias
        subjects = [
            self.subject("C202", "Computer Science II", 101, self.db),
            self.subject("C206", "Data Structures", 102, self.db),
            self.subject("C201", "Introduction to Programming", 103, self.db),
            self.subject("E201", "Engineering Mathematics", 104, self.db),
            self.subject("C005", "Digital Logic", 101, self.db),
        ]
        for subject in subjects:
            subject.create_subject()

        # Criando notas
        grades = [
            self.grade(1, 85.0, "C202", 101, self.db),
            self.grade(2, 90.0, "C206", 102, self.db),
            self.grade(3, 95.0, "C201", 103, self.db),
            self.grade(4, 88.0, "E201", 104, self.db),
            self.grade(5, 92.0, "C005", 101, self.db),
            self.grade(6, 92.0, "C202", 101, self.db),
            self.grade(7, 85.0, "C206", 102, self.db),
        ]
        for grade in grades:
            grade.create_grade()

        # Relacionando estudantes com matérias e professores
        relationships = [
            (students[0], subjects[0], teachers[0]),  # Matheus Fonseca -> C202 -> Yvo
            (students[0], subjects[1], teachers[1]),  # Matheus Fonseca -> C206 -> Renzo
            (students[1], subjects[1], teachers[1]),  # Alvaro Lucio -> C206 -> Renzo
            (students[1], subjects[0], teachers[0]),  # Alvaro Lucio -> C202 -> Yvo
            (students[2], subjects[2], teachers[2]),  # Thiago Rocha -> C201 -> Chris
            (students[2], subjects[1], teachers[1]),  # Thiago Rocha -> C206 -> Renzo
            (students[2], subjects[3], teachers[3]),  # Thiago Rocha -> E201 -> Ewel
            (students[3], subjects[3], teachers[3]),  # Pedro Luis -> E201 -> Ewel
            (students[3], subjects[2], teachers[2]),  # Pedro Luis -> C201 -> Chris
        ]
        for student, subject, teacher in relationships:
            student.add_subject(subject)
            student.add_teacher(teacher)

        # Relacionando estudantes com notas
        grade_relationships = [
            (students[0], grades[0]),  # Matheus Fonseca -> Grade 1
            (students[1], grades[1]),  # Alvaro Lucio -> Grade 2
            (students[2], grades[2]),  # Thiago Rocha -> Grade 3
            (students[3], grades[3]),  # Pedro Luis -> Grade 4
            (students[0], grades[5]),  # Matheus Fonseca -> Grade 6
            (students[1], grades[6]),  # Alvaro Lucio -> Grade 7
        ]
        for student, grade in grade_relationships:
            student.add_grade(grade)

        # Relacionando professores com matérias
        for subject in subjects:
            teacher = next(
                (t for t in teachers if t.teacher_id == subject.teacher_id), None
            )
            if teacher:
                teacher.add_subject(subject)
