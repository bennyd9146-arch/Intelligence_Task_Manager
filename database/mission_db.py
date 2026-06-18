from db_connction import connection
connection.connect(
    host= "127.0.0.1",
    user = "root",
    port=3306,
    password= "1234",
    database = "Intelligence_db"
                )
def create_mission(body:dict):


    try:    
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""insert into missions(id,titel,description,location,difficulty,importance,status,level_risk,assigned_agent_id) 
                    values(%s, %s, %s, %s, %s, %s, %s, %s, %s);""",(body["id"],body["titel"],body["description"],
                    body["location"],body["difficulty"],body["importance"],body["status"],body["level_risk"],body["assigned_agent_id"],))
                
                
        connection.commit()
        return cursor.fetchall()

    except Exception as e:
        print(e)

    finally:
        cursor.close()

def get_all_missions():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select * from missions")
    return cursor.fetchall()
    


def get_mission_by_id():
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("select * from missions where id = %s")
        return cursor.fetchall()
    except Exception as e:
        print(e)
    

    finally:
        cursor.close()
