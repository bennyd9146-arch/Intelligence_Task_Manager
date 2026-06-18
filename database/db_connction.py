from mysql import connector

connection = connector.connect(
    host= "127.0.0.1",
    user = "root",
    port=3306,
    password= "1234",
    database = "Intelligence_db"
                )
def create_database():
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""create database 
                    if not exists Intelligence_db
                    """)
        
        cursor.execute("use Intelligence_db")

def create_tables():

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""CREATE table if not EXISTS agents(
                    id int AUTO_INCREMENT PRIMARY key,
                    name VARCHAR(100),
                    specialty VARCHAR(200),
                    is_active BOOLEAN DEFAULT true,
                    completed_missions INT DEFAULT 0,
                    failed_missions int DEFAULT 0,
                    agent_rank  ENUM("Junior","Senior" ,"Commander") DEFAULT "Junior"
                );""")
     
        cursor.execute("""create table if not exists  missions(
                id int AUTO_INCREMENT PRIMARY key,
                title VARCHAR(100),
                description TEXT,
                location VARCHAR(100),
                difficulty int ,
                importance int ,
                status varchar(100) DEFAULT "NEW",
                risk_level varchar(100),
                assigned_agent_id int DEFAULT NULL
                );""")
            
        connection.commit()

    except Exception as e:
        print(e)

   
    
        
def get_connection():
    if connection.is_connected:
         connection.close()

create_database()
create_tables()
get_connection()