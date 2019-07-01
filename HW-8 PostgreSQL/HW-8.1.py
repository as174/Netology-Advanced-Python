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
            student_id INTEGER REFERENCES student(id),
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
    cur.execute("SELECT * FROM student WHERE id = (s.id) VALUES (%s)", (student_id))
    return(cur.fetchall())
    conn.commit()
    cur.close()
    
def add_students(course_id, students): 

    conn = psycopg2.connect(config)
    cur = conn.cursor()
    for student in students:
        cur.execute("INSERT INTO student (name, gpa, birth) VALUES (%s, %s, %s)", 
                    (student['name'], student['gpa'], student['birth']))
        cur.execute("INSERT INTO student_course (student_id, course_id) VALUES (%s, %s)", 
                    (student.id), (course.id))
    conn.commit()
    cur.close()                              
    pass    

def get_students(course_id): # возвращает студентов определенного курса
    
    conn = psycopg2.connect(config)
    cur = conn.cursor()
    cur.execute("SELECT student.name, course.id FROM student_course `\
                join student on student_course.student_id = student.id `\
                join course on student_course.course_id = course.id")
    return(cur.fetchall())
    conn.commit()
    cur.close()


if __name__ == '__main__':
    config = 'dbname=netology_db user=admin'
#    create_db()
#    
#    student_1 = {'name': 'test1 testovich1', 'gpa': '1.1', 'birth': '1991-01-01 11:30'}
#    student_2 = {'name': 'test2 testovich2', 'gpa': '2.2', 'birth': '1992-02-02 11:30'}
#    student_3 = {'name': 'test3 testovich3', 'gpa': '3.3', 'birth': '1993-03-03 11:30'}
#    student_4 = {'name': 'tes4 testovich4', 'gpa': '4.4', 'birth': '1994-04-04 11:30'}
#    
#    
#    python = 'python'
#    php = 'php'
    
#    add_course(python)
#    add_course(php)
    
#    add_student(student_4)
    
#    conn = psycopg2.connect(config)
#    cur = conn.cursor()
#    cur.execute("select * from course")
#    print(cur.fetchall())
    
#
#    conn = psycopg2.connect(config)
#    cur = conn.cursor()
#    cur.execute("SELECT * FROM student WHERE id = 3")
#    print(cur.fetchall()) 

    a = get_student(1)
    print(a)