from connection import Connection


class Sqlqueries:
    def __init__(self):
        self.query_db = Connection()
        

    def create_query(self):
        
        conn,cursor = self.query_db.create_conn()
        if conn is None:
            return False
        try:
            print("kindly enter your credentials")
            name = str(input("enter your name:"))
            marks = float(input("enter your marks:"))
            grade = str(input("enter your grade:"))
            section = str(input("enter your section (e.g., A1):"))
            project = str(input("enter your project:"))
            query = """INSERT INTO stud(name,marks,grade,section,project)VALUES(%s,%s,%s,%s,%s)"""
            values =(name,marks,grade,section,project)
            cursor.execute(query,values)
            conn.commit()
            print("value stored successfully!")
            return True

        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()

    def view_all(self):
        conn,cursor = self.query_db.create_conn()
        if conn is None:
            return False
        
        try:
            query = """SELECT * FROM stud;"""
            cursor.execute(query)
            data = cursor.fetchall()

            if not data:
                print("No records found")
                return False
            
            for i in data :
                print(i)
            return True
        
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()
    
    def id(self):
        conn,cursor = self.query_db.create_conn()
        if conn is None:
            return False
        try:
            rollno = int(input("enter your roll number:"))
            query =(f"SELECT * FROM stud WHERE rollno =%s")
            cursor.execute(query,(rollno,))
            data = cursor.fetchone()
            print('id,name,marks,grade,section,project')
            print(data)
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()

    def update_stud(self):
        conn,cursor = self.query_db.create_conn()
        if conn is 'None':
            return False
        try:
            field = str(input("which field to update:"))
            valid_fields = ['name','marks','grade','section','project']
            if field not in valid_fields:
                raise ValueError("kindly select the valid fileds",valid_fields)
                return False
            oldvalue = str(input(f"enter the old value of {field}:"))
            newvalue = str(input(f"enter the new value of {field}:"))
            query =f"""UPDATE stud SET {field} = %s WHERE {field}=%s"""
            values=(newvalue,oldvalue)
            cursor.execute(query,values)
            conn.commit()
            if cursor.rowcount == 0:
                return False
            print("value updated successfully!")
            return True
        
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()

    def delete_stud(self):
        conn,cursor = self.query_db.create_conn()
        if conn is None:
            return False
        try:
            field = input("enter the field with which you wish to delete the record: ")
            valid_fields = ['rollno','name']
            if field not in valid_fields:
                print(f"kindly enter the valid field{valid_fields}")
                return False
            if field =='rollno':
                value = int(input("enter the roll number you want to delete : "))
            elif field == 'name':
                value = str(input("enter the name you want to delete : "))
            query = f"""DELETE FROM stud WHERE {field} = %s"""
            cursor.execute(query,(value,))
            conn.commit()
            
            if cursor.rowcount == 0:
                print("No record found to delete")
                return False
            else:
                print("Record deleted successfully")
                return True
        
        except Exception as e:
            print("error",e)
            return False

        finally:
            cursor.close()
            conn.close()



        



