class Teacher:
    def __init__(self, teacher_id, name, db):
        self.teacher_id = teacher_id
        self.name = name
        self.db = db

    def create_teacher(self):
        query = """
                MERGE (t:Teacher {teacher_id: $teacher_id, name: $name})
                """
        parameters = {"teacher_id": self.teacher_id, "name": self.name}
        self.db.execute_query(query, parameters)

    def add_subject(self, subject):
        query = """
                MATCH (t:Teacher {teacher_id: $teacher_id})
                MATCH (sub:Subject {subject_id: $subject_id})
                MERGE (t)-[:TEACHES]->(sub)
                """
        parameters = {"teacher_id": self.teacher_id, "subject_id": subject.subject_id}
        self.db.execute_query(query, parameters)
