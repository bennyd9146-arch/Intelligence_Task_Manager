from db_connction import connection
class AgentDB:
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
    
    def agents_all_get():
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("select * from Intelligence_db;")
            return cursor.fetchall()
        
        except Exception as e:
            print(e)


        finally:
            cursor.close()

    
    def get_agent_by_id(id):
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("select * from agents where id = %s;")
            return cursor.fetchall()
        except Exception as e:
            print(e)

        finally:
            cursor.close()

    def updete_agent(id):
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("update ")
            return cursor.fetchall()
            
        except Exception as e:
            print(e)

        finally:
            cursor.close()