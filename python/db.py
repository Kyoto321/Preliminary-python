# 6.      Save the colours and their frequencies in postgresql database
 
import psycopg2

# connect to postgres 

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
    port= '5432'
)

cursor = connection.cursor()

# create database table 

table_creation = """
   CREATE TABLE WORK_OUTFIT (
       ID SERIAL PRIMARY KEY,
       DAYS TEXT NOT NULL,
       COLOURS TEXT NOT NULL
   )
"""
cursor.execute(table_creation)

# insert data into postgres database

postgres_insert_query = """ INSERT INTO mobile (ID, DAYS, COLOURS) VALUES (%s,%s,%s)"""
record_to_insert = (1, 'MONDAY', 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'),
(2, 'TUESDAY', 'ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE'),
(3, 'WEDNESSDAY', 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE'),
(4, 'THURSDAY', 'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN'),
(5, 'FRIDAY', 'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE')
                    
cursor.execute(postgres_insert_query, record_to_insert)


connection.commit()
cursor.close()
connection.close()


