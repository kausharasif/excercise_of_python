import os
import shutil
class FileOperation:
    def __init(self):
        self.fn = None
    def open(self,FileName,mode='r'):
        try:
            self.fn=open(FileName,mode)
            print(f"File Opened {FileName}")
            return True
        except FileNotFoundError:
            print(f"File {FileName} does not exist")
            return False
    def write(self,content):
        if self.fn == None:
           return False
        else:
            self.fn.write(content)
            print("File saved")
            return True
