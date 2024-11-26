class Grade:
    def __init__(self, grade_id, obtained_grade, subject_id, teacher_id, db):
        self.grade_id = grade_id
        self.obtained_grade = obtained_grade
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.db = db

    def create_grade(self):
        query = """
                MERGE (g:Grade {grade_id: $grade_id, obtained_grade: $obtained_grade, subject_id: $subject_id, teacher_id: $teacher_id})
                """
        parameters = {
            "grade_id": self.grade_id,
            "obtained_grade": self.obtained_grade,
            "subject_id": self.subject_id,
            "teacher_id": self.teacher_id,
        }
        self.db.execute_query(query, parameters)
