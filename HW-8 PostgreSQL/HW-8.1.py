import psycopg2

def create_db(): 
    
    commands = (
            """
            CREATE TABLE student (
            id serial PRIMARY KEY not null,
            name varchar(100) not null,
            gpa numeric(10,2),
            birth timestamp with time zone)
            """,
            """
            CREATE TABLE course (
            id serial PRIMARY KEY not null,
            name varchar(100) not null)
            """,
            """
            CREATE TABLE student_course (
            id serial PRIMARY KEY,
            student_id INTEGER REFERENCES student(id) not null,
            course_id INTEGER REFERENCES course(id))
            """)
    conn = psycopg2.connect(config)
    cur = conn.cursor() 
    for c in commands:
        cur.execute(c)
    conn.commit()
    cur.close()


def add_student(student):
    
    conn = psycopg2.connect(config)
    cur = conn.cursor()
    cur.execute("INSERT INTO student (name, gpa, birth) VALUES (%s, %s, %s)", 
    (student['name'], student['gpa'], student['birth']))
    conn.commit()
    cur.close()
    print(student, 'добавлен')

def add_course(course_name):
    
    conn = psycopg2.connect(config)
    cur = conn.cursor()
    cur.execute("INSERT INTO course (name) VALUES (%s)", (course_name, ))
    conn.commit()
    cur.close()    
    
def get_student(student_id):
    
    conn = psycopg2.connect(config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE id = %s", (student_id, ))
    return(cur.fetchall())
    conn.commit()
    cur.close()
    
def add_students(course_id, students): 

    conn = psycopg2.connect(config)
    cur = conn.cursor()
    for student in students:
        cur.execute("INSERT INTO student (name, gpa, birth) VALUES (%s, %s, %s)", 
                    (student['name'], student['gpa'], student['birth']))
        cur.execute("SELECT id from student WHERE name = %s", (student['name'], ))
        cur.execute("SELECT lastval()")
        student_id = cur.fetchone()
        cur.execute("INSERT INTO student_course (student_id, course_id) VALUES (%s, %s)", 
                    (student_id, course_id, ))
        conn.commit()
    cur.close()                              
        

def get_students(course_id): # возвращает студентов определенного курса
    
    conn = psycopg2.connect(config)
    cur = conn.cursor()
    cur.execute("""SELECT student.name FROM student_course 
                JOIN student on student.id = student_course.student_id 
                JOIN course on course.id = student_course.course_id 
                WHERE course.id = %s""", (course_id, ))

    return(cur.fetchall())
    conn.commit()
    cur.close()


if __name__ == '__main__':
    config = 'dbname=netology_db user=test password=123'
