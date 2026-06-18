from .db_connction import connection
connection.connect(
    host= "127.0.0.1",
    user = "root",
    port=3306,
    password= "1234",
    database = "Intelligence_db"
                )
def create_agent(body:dict):
        try:
            
            cursor = connection.cursor(dictionary=True)
            cursor.execute("""insert into agents(id,name,specialty,is_active,completed_missions,failed_missions,agent_rank) 
                values(%s, %s, %s, %s, %s, %s, %s);""",(body["id"],body["name"],body["specialty"],body["is_active"],body["completed_missions"],body["failed_missions"],body["agent_rank"],))
            
            
            connection.commit()
            return cursor.fetchall()

        except Exception as e:
            print(e)
        finally:
            cursor.close()
    
def all_get_agents():
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("select * from Intelligence_db;")
            return cursor.fetchall()
            
        except Exception as e:
            print(e)


    
    
def get_agent_by_id(id):
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("select * from agents where id = %s;")
            return cursor.fetchall()
        except Exception as e:
            print(e)

        cursor.close()
        
def updete_agent(body,id):
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("update agents set name = %s where id = %s")
            return cursor.fetchall()
            
        except Exception as e:
            print(e)

        finally:
            cursor.close()

def agent_deactivate(id):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("")
        return cursor.fetchall()
    except Exception as e:
         print(e)
        
    finally:
         cursor.close()