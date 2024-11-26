class ModulesViewData:
    def __init__(self, db):
        self.db = db

    def get_students(self, registration=None, name=None, course=None):
        filters = []
        parameters = {}

        if registration:
            filters.append("s.registration_number = $registration")
            parameters["registration"] = int(
                registration
            )  # Certifique-se de converter para int

        if name:
            filters.append("s.name = $name")
            parameters["name"] = name

        if course:
            filters.append("s.course = $course")
            parameters["course"] = course

        where_clause = "WHERE " + " AND ".join(filters) if filters else ""

        query = f"""
        MATCH (s:Student)
        {where_clause}
        RETURN s.name AS Name, s.registration_number AS Registration, s.course AS Course
        """
        return self.db.execute_query(query, parameters)

    def get_teachers(self, registration=None, name=None):
        filters = []
        parameters = {}

        if registration:
            filters.append("t.teacher_id = $registration")
            parameters["registration"] = int(
                registration
            )  # Certifique-se de converter para int

        if name:
            filters.append("t.name = $name")
            parameters["name"] = name

        where_clause = "WHERE " + " AND ".join(filters) if filters else ""

        query = f"""
        MATCH (t:Teacher)
        {where_clause}
        RETURN t.name AS Name, t.teacher_id AS Registration
        """
        return self.db.execute_query(query, parameters)

    def get_subjects(self, subject_id=None, subject_name=None, teacher_name=None):
        filters = []
        parameters = {}

        if subject_id:
            filters.append("sub.subject_id = $subject_id")
            parameters["subject_id"] = subject_id

        if subject_name:
            filters.append("sub.name = $subject_name")
            parameters["subject_name"] = subject_name

        if teacher_name:
            filters.append("t.name = $teacher_name")
            parameters["teacher_name"] = teacher_name

        where_clause = "WHERE " + " AND ".join(filters) if filters else ""

        query = f"""
        MATCH (sub:Subject)-[:TEACHES]-(t:Teacher)
        {where_clause}
        RETURN sub.name AS SubjectName, sub.subject_id AS SubjectID, t.name AS TeacherName
        """
        return self.db.execute_query(query, parameters)

    def get_grades(self, student_name=None, course_name=None):
        filters = []
        parameters = {}

        # Adicionar filtros dinamicamente
        if student_name:
            filters.append("s.name = $student_name")
            parameters["student_name"] = student_name

        if course_name:
            filters.append("s.course = $course_name")
            parameters["course_name"] = course_name

        # Construção do WHERE dinamicamente
        where_clause = "WHERE " + " AND ".join(filters) if filters else ""

        query = f"""
        MATCH (s:Student)-[:RECEIVES]->(g:Grade)
        MATCH (sub:Subject {{subject_id: g.subject_id}})
        {where_clause}
        RETURN s.name AS StudentName, s.course AS Course, g.obtained_grade AS Grade, sub.name AS SubjectName
        """
        return self.db.execute_query(query, parameters)
