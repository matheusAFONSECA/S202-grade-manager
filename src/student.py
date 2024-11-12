class Student:
    def __init__(self, registration_number, course, name, db):
        self.registration_number = registration_number
        self.course = course
        self.name = name
        self.db = db

    def create_student(self):
        query = """
    MERGE (s:Student {registration_number: $registration_number, course: $course, name: $name})
    """
        parameters = {"registration_number": self.registration_number, "course": self.course, "name": self.name}
        self.db.execute_query(query, parameters)

    def add_grade(self, grade):
        query = """
    MATCH (s:Student {registration_number: $registration_number})
    MATCH (g:Grade {grade_id: $grade_id})
    MERGE (s)-[:RECEIVES]->(g)
    """
        parameters = {"registration_number": self.registration_number, "grade_id": grade.grade_id}
        self.db.execute_query(query, parameters)

    def add_teacher(self, teacher):
        query = """
    MATCH (s:Student {registration_number: $registration_number})
    MATCH (t:Teacher {teacher_id: $teacher_id})
    MERGE (s)-[:IS_TAUGHT_BY]->(t)
    """
        parameters = {"registration_number": self.registration_number, "teacher_id": teacher.teacher_id}
        self.db.execute_query(query, parameters)

    def add_subject(self, subject):
        query = """
    MATCH (s:Student {registration_number: $registration_number})
    MATCH (sub:Subject {subject_id: $subject_id})
    MERGE (s)-[:STUDIES]->(sub)
    """
        parameters = {"registration_number": self.registration_number, "subject_id": subject.subject_id}
        self.db.execute_query(query, parameters)
