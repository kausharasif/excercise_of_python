from http import server
from mysql import connector as con
from mysql.connector import ProgrammingError
from mysql.connector import InterfaceError
from MyFileOperation import FileOperation 
import common_functions as cf
class MyDatabase:
    def __init__(self,database,username='root',password='',port=3306,server='localhost',script=None):
        try:
            self.database = database
            self.username = username
            self.password = password
            self.port = port
            self.server = server
            self.script = script
            self.db = con.connect(host=self.server,user=self.username,passwd=self.password,
            database=self.database,port=self.port)
            print("connection established....")
            self.file = FileOperation()
            self.file.open("error.log","a")
        except ProgrammingError:
            print ("database connection failed please check ")
            print ("1) ensure database server is on")
            print ("2) check password and database name ")
        except InterfaceError:
            print ("database connection failed")
            print ("verify username, port no")
    def RunQuery(self,sql,values=None): #used for insert,update,delete etc query any query except select
        try:
            self.sqlcommand = self.db.cursor()
            if values == None:
                self.sqlcommand.execute(sql)
            else:
                self.sqlcommand.execute(sql,values)
            self.db.commit()
            return True
        except ProgrammingError as e:
            self.LogError(e)
            return False
    def LogError(self,e):
        cdt = str(cf.GetDate()) + " "  + str(cf.GetTime()) #return current date in indian format
        message = f"""
        Error No = {e.errno}
        Short Description = {e.msg}
        Full Description = {e._full_msg}
        File Name = {self.script}
        Error DateTime = {cdt}
        """
        self.file.write(message)
    def FetchRow(self,sql,values=None):
        try:
            self.sqlcommand = self.db.cursor(dictionary = True)
            table = None
            if values == None:
                table = self.sqlcommand.execute(sql)
            else:
                table = self.sqlcommand.execute(sql,values)
            table = self.sqlcommand.fetchall()
            return table
        except ProgrammingError as e:
            self.LogError(e)
            return False







