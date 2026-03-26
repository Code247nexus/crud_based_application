
from queries import Sqlqueries
#CRUD APPPLICATION
#1)CREATE
# 2)RETRIEVE
# 3)UPDATE
# 4)DELETE
class Main:
    def __init__(self):
        self.qy = Sqlqueries()
    

    def menu(self):
        while True:
            user_input = input("""
        1. Add Student
        2. View All Students
        3. View Student by ID
        4. Update Student
        5. Delete Student
        6. Exit :""")

            if  user_input == '1':
                self.Create()
            elif user_input == '2':
                self.Viewall()
            elif user_input == '3':
                self.Viewstudid()
            elif user_input =='4':
                self.Update()
            elif user_input == '5':
                self.Delete()
            elif user_input =='6':
                print("Exiting")
                break
            else:
                print("invalid choice")

    
    def Create(self):
        flag = self.qy.create_query()
        if flag :
            print("command executed")
        else:
            print("operation failed!")

    def Viewall(self):
        flag = self.qy.view_all()
        if flag:
            print("command executed")
        else:
            print("operation failed!")

    def Viewstudid(self):
        flag = self.qy.id()
        if flag:
            print("command executed!")
        else:
            print("operation failed!")
    def Update(self):
        flag = self.qy.update_stud()
        if flag:
            print("command executed!")
        else:
            print("operation failed!")
    def Delete(self):
        flag = self.qy.delete_stud()
        if flag:
            print("command executed!")
        else:
            print("operation failed")


if __name__ =='__main__':
        app=Main()
        app.menu()