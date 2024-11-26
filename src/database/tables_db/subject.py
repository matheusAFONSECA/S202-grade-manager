class Subject:
    def __init__(self, subject_id, name, teacher_id, db):
        self.subject_id = subject_id
        self.name = name
        self.teacher_id = teacher_id
        self.db = db

    def create_subject(self):
        query = """
                MERGE (sub:Subject {subject_id: $subject_id, name: $name, teacher_id: $teacher_id})
                """
        parameters = {
            "subject_id": self.subject_id,
            "name": self.name,
            "teacher_id": self.teacher_id,
        }
        self.db.execute_query(query, parameters)
