// Criando alunos
MERGE (s1:Student {registration_number: 1, course: "Computer Science", name: "Matheus Fonseca"})
MERGE (s2:Student {registration_number: 2, course: "Computer Science", name: "Alvaro Lucio"})
MERGE (s3:Student {registration_number: 3, course: "Computer Science", name: "Thiago Rocha"})
MERGE (s4:Student {registration_number: 4, course: "Computer Science", name: "Pedro Luis"})

// Criando professores
MERGE (t1:Teacher {teacher_id: 101, name: "Yvo"})
MERGE (t2:Teacher {teacher_id: 102, name: "Renzo"})
MERGE (t3:Teacher {teacher_id: 103, name: "Chris"})
MERGE (t4:Teacher {teacher_id: 104, name: "Ewel"})

// Materias
MERGE (sub1:Subject {subject_id: "C202", name: "Computer Science II", teacher_id: 101})
MERGE (sub2:Subject {subject_id: "C206", name: "Data Structures", teacher_id: 102})
MERGE (sub3:Subject {subject_id: "C201", name: "Introduction to Programming", teacher_id: 103})
MERGE (sub4:Subject {subject_id: "E201", name: "Engineering Mathematics", teacher_id: 104})
MERGE (sub5:Subject {subject_id: "C005", name: "Digital Logic", teacher_id: 101})

// Notas
MERGE (g1:Grade {grade_id: 1, obtained_grade: 85.0, subject_id: "C202", teacher_id: 101})
MERGE (g2:Grade {grade_id: 2, obtained_grade: 90.0, subject_id: "C206", teacher_id: 102})
MERGE (g3:Grade {grade_id: 3, obtained_grade: 95.0, subject_id: "C201", teacher_id: 103})
MERGE (g4:Grade {grade_id: 4, obtained_grade: 88.0, subject_id: "E201", teacher_id: 104})
MERGE (g5:Grade {grade_id: 5, obtained_grade: 92.0, subject_id: "C005", teacher_id: 101})
MERGE (g6:Grade {grade_id: 6, obtained_grade: 92.0, subject_id: "C202", teacher_id: 101})
MERGE (g7:Grade {grade_id: 7, obtained_grade: 85.0, subject_id: "C206", teacher_id: 102})

// Relacionando os alunos com as materias e professores
MATCH (s:Student {name: "Matheus Fonseca"}), (sub:Subject {subject_id: "C202"}), (t:Teacher {teacher_id: 101})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Matheus Fonseca"}), (sub:Subject {subject_id: "C206"}), (t:Teacher {teacher_id: 102})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Alvaro Lucio"}), (sub:Subject {subject_id: "C206"}), (t:Teacher {teacher_id: 102})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Alvaro Lucio"}), (sub:Subject {subject_id: "C202"}), (t:Teacher {teacher_id: 101})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Thiago Rocha"}), (sub:Subject {subject_id: "C201"}), (t:Teacher {teacher_id: 103})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Thiago Rocha"}), (sub:Subject {subject_id: "C206"}), (t:Teacher {teacher_id: 102})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Thiago Rocha"}), (sub:Subject {subject_id: "E201"}), (t:Teacher {teacher_id: 104})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Pedro Luis"}), (sub:Subject {subject_id: "E201"}), (t:Teacher {teacher_id: 104})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

MATCH (s:Student {name: "Pedro Luis"}), (sub:Subject {subject_id: "C201"}), (t:Teacher {teacher_id: 103})
MERGE (s)-[:STUDIES]->(sub)
MERGE (s)-[:IS_TAUGHT_BY]->(t);

// Relacionando os alunos com suas notas
MATCH (s:Student {name: "Matheus Fonseca"}), (g:Grade {grade_id: 1})
MERGE (s)-[:RECEIVES]->(g);

MATCH (s:Student {name: "Alvaro Lucio"}), (g:Grade {grade_id: 2})
MERGE (s)-[:RECEIVES]->(g);

MATCH (s:Student {name: "Thiago Rocha"}), (g:Grade {grade_id: 3})
MERGE (s)-[:RECEIVES]->(g);

MATCH (s:Student {name: "Pedro Luis"}), (g:Grade {grade_id: 4})
MERGE (s)-[:RECEIVES]->(g);

MATCH (s:Student {name: "Matheus Fonseca"}), (g:Grade {grade_id: 6})
MERGE (s)-[:RECEIVES]->(g);

MATCH (s:Student {name: "Alvaro Lucio"}), (g:Grade {grade_id: 7})
MERGE (s)-[:RECEIVES]->(g);

// Relacionando os professores com as materias
MATCH (t:Teacher {teacher_id: 101}), (sub:Subject {subject_id: "C202"})
MERGE (t)-[:TEACHES]->(sub);

MATCH (t:Teacher {teacher_id: 102}), (sub:Subject {subject_id: "C206"})
MERGE (t)-[:TEACHES]->(sub);

MATCH (t:Teacher {teacher_id: 103}), (sub:Subject {subject_id: "C201"})
MERGE (t)-[:TEACHES]->(sub);

MATCH (t:Teacher {teacher_id: 104}), (sub:Subject {subject_id: "E201"})
MERGE (t)-[:TEACHES]->(sub);

MATCH (t:Teacher {teacher_id: 104}), (sub:Subject {subject_id: "C005"})
MERGE (t)-[:TEACHES]->(sub);
