from DBOperation import MyDatabase
import datetime
db1 = MyDatabase(database='management_system_python',script=__file__)
def ConvertDatetoDMY(mydate):
    converted_date = datetime.datetime.strptime(
        mydate, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
    return converted_date
def DisplayCourseDetails():
    sql = "select * from course_management where isDeleted=0"
    table = db1.FetchRow(sql)
    if table == False:
        print("Error Occured")
    else:
        heading = f"{'id':2}|{'title':32}|{'fees':12}|{'duration':12}|{'description':73}"
        print(heading)
        for row in table:
            print('-'*100)
            output = f"{row['id']:2}|{row['title']:32}|{row['fees']:12}|{row['duration']:12}|{row['description']:73}"
            print(output)
        print("-"*100)
def DisplayBatchDetails():
    sql = "select b.*,c.title 'coursename' from course_management c,batch_management b where b.courseid=c.id and b.isDeleted=0"
    table = db1.FetchRow(sql)
    if table == False:
        print("Error Occured")
    else:
        heading = f"{'id':2}|{'courseid':2}|{'startdate':25}|{'enddate':25}|{'classtime':12}|{'course Name':40}|{'title':25}"
        print(heading)
        for row in table:
            row['startdate'] = ConvertDatetoDMY(str(row['startdate']))
            row['enddate'] = ConvertDatetoDMY(str(row['enddate']))
            print('-'*100)
            output = f"{row['id']:2}|{row['courseid']:2}|{row['startdate']:25}|{row['enddate']:25}|{row['classtime']:12}|{row['coursename']:40}|{row['title']:25}"
            print(output)
        print("-"*100)
def DisplaySubjectDetails():
    sql="select s.*,c.title 'coursename' from subject_management s,course_management c where s.courseid=c.id and s.isDeleted=0"
    table = db1.FetchRow(sql)
    if table == False:
        print("Error Occured")
    else:
        heading = f"{'id':2}|{'courseid':2}|{'CourseName':25}|{'title':25}|{'rate':12}"
        print(heading)
        for row in table:
            print('-'*100)
            output = f"{row['id']:2}|{row['courseid']:2}|{row['coursename']:25}|{row['title']:25}|{row['rate']:12}"
            print(output)
    print('-'*100)
def DisplayTeacherDeatils():
    sql = "select * from teacher_management where isDeleted=0"
    table = db1.FetchRow(sql)
    if table == False:
        print("Error Occured")
    else:
        heading = f"{'id':2}|{'name':25}|{'mobile':15}|{'email':30}|{'gender':8}|{'qualification':25}|{'experience':20}"
        print(heading)
        for row in table:
            print('-'*100)
            output = f"{row['id']:2}|{row['name']:25}|{row['mobile']:15}|{row['email']:30}|{row['gender']:8}|{row['qualification']:25}|{row['experience']:20}"
            print(output)
    print('-'*100)
while 1:
    print('-'*100)
    print("1 for course Management")
    print("2 for Batch management")
    print("3 for subject details")
    print("4 for teacher details")
    print("5 for lecture management")
    print("6 for payout management")
    print("7 for reports")
    print("Press 0 for for exit")
    ModuleChoice= int(input("Enter choice"))
    if ModuleChoice==1:
        while 1:
            print("1 for inserting the course")
            print("2 for updating the course")
            print("3 for deleting the course")
            print("4 for fetching the course details")
            print("0 for exit")
            CourseChoice = int(input("Enter course choice"))
            if CourseChoice == 1:
                print("Enter course details")
                title = input("Enter course Title")
                fees = int(input("Enter courses fees"))
                duration = input("Enter duration")
                description = input("Enter description")
                sql = "insert into course_management (title,fees,duration,description) values (%s,%s,%s,%s)"
                values= [title,fees,duration,description]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Course Details Added")
                else:
                    print("Error Occured")
            elif CourseChoice == 2:
                DisplayCourseDetails()
                courseid = int(input("Enter course id"))
                title = input("Enter course Title")
                fees = int(input("Enter courses fees"))
                duration = input("Enter duration")
                description = input("Enter description")
                sql = "update course_management set title=%s,fees=%s,duration=%s,description=%s where id=%s"
                values = [title,fees,duration,description,courseid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Course Details Updated")
                else:
                    print("Error Occured")
            elif CourseChoice == 3:
                DisplayCourseDetails()
                courseid = int(input("Enter course id"))
                sql = "update course_management set isDeleted=1 where id=%s"
                values = [courseid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Course Details Deleted")
                else:
                    print("Error Occured")
            elif CourseChoice == 4:
                DisplayCourseDetails()
            elif CourseChoice == 0:
                break
            else:
                print("Please choose the number between 0-4")
    elif ModuleChoice == 2:
        while 1:
            print("1 for inserting batch details")
            print("2 for updating batch details")
            print("3 for deleting batch details")
            print("4 for fetching batch details")
            print("0 for exit")
            BatchChoice= int(input("Enter choice"))
            if BatchChoice==1:
                print("Enter batch details")
                DisplayCourseDetails()
                courseid = int(input("Enter course id"))
                startdate = input("Enter start date (YYYY-MM-DD)")
                enddate = input("Enter end date (YYYY-MM-DD)")
                classtime = input("Enter class time")
                title = input("Enter tile")
                sql = "insert into batch_management (courseid,startdate,enddate,classtime,title) values(%s,%s,%s,%s,%s)"
                values = [courseid,startdate,enddate,classtime,title]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Batch details added")
                else:
                    print("Error Occured")
            elif BatchChoice == 0:
                break
            elif BatchChoice == 2:
                print("Below information show the details of courses")
                DisplayCourseDetails()
                print("Below information show the details of batches")
                DisplayBatchDetails()
                batchid = int(input("enter batch id"))
                courseid = int(input("Enter course id"))
                startdate = input("Enter start date (YYYY-MM-DD)")
                enddate = input("Enter end date (YYYY-MM-DD)")
                classtime = input("Enter class time")
                title = input("Enter tile")
                sql = "update batch_management set courseid=%s,startdate=%s,enddate=%s,classtime=%s,title=%s where id=%s"
                values = [courseid,startdate,enddate,classtime,title,batchid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Batch details Updated")
                else:
                    print("Error Occured")
            elif BatchChoice == 3:
                print("Below information show the details of batches")
                DisplayBatchDetails()
                batchid = int(input("Enter batch id"))
                sql ="update batch_management set isDeleted=1 where id = %s"
                values= [batchid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Batch details deleted")
                else:
                    print("Error Occured")
            elif BatchChoice == 4:
                DisplayBatchDetails()
            else:
                print("Please choose the number between 0-4")
    elif  ModuleChoice == 3:
        while 1:
            print("1 for enter subject details")
            print("2 for updating subject details")
            print("3 for deleting subject details")
            print("4 displaying subject details")
            print("0 for exit")
            SubjectChoice = int(input("Enter Choice"))
            if SubjectChoice == 1:
                print("Below information show the details of courses")
                DisplayCourseDetails()
                courseid = int(input("Enter courseid"))
                title = input("Enter title of the subject")
                rate = int(input("Enter the rate for the subject"))
                sql = "insert into subject_management (courseid,title,rate) values (%s,%s,%s)"
                values = [courseid,title,rate]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Subject details added")
                else:
                    print("Error Occured")
            elif SubjectChoice == 0:
                break
            elif SubjectChoice == 4:
                DisplaySubjectDetails()
            elif SubjectChoice == 2:
                print("Below show the details of the courses")
                DisplayCourseDetails()
                print("Below show the details of teh subjects")
                DisplaySubjectDetails()
                subjectid = int(input("Enter subject id"))
                courseid = int(input("Enter courseid"))
                title = input("Enter title of the subject")
                rate = int(input("Enter the rate for the subject"))
                sql = "update subject_management set courseid=%s,title=%s,rate=%s where id=%s"
                values= [courseid,title,rate,subjectid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Subject details Edited")
                else:
                    print("Error Occured")
            elif SubjectChoice == 3:
                print("Below show the details of teh subjects")
                DisplaySubjectDetails()
                subjectid = int(input("Enter subject id"))
                sql = "update subject_management set isDeleted=1 where id=%s"
                values= [subjectid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Subject details Deleted")
                else:
                    print("Error Occured")
            else:
                print("Please choose the number between 0-4")
    elif ModuleChoice == 4:
        while 1:
            print("1 for inserting Teacher details")
            print("2 for updating teacher details")
            print("3 for deleting teacher details")
            print("4 displaying teacher details")
            print("0 for exit")
            TeacherChoice= int(input("Enter choice"))
            if TeacherChoice == 1:
                name = input("Enter name")
                mobile = input("Enter mobile")
                email = input("Enter email")
                gender = input("enter gender")
                qualification = input("Enter qualification")
                experience = input("Enter experience")
                sql = "insert into teacher_management (name,mobile,email,gender,qualification,experience) values (%s,%s,%s,%s,%s,%s)"
                values = [name,mobile,email,gender,qualification,experience]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Teacher details added")
                else:
                    print("Error Occured")
            elif TeacherChoice == 0:
                break
            elif TeacherChoice == 4:
                DisplayTeacherDeatils()
            elif TeacherChoice == 2:
                DisplayTeacherDeatils()
                teacherid = int(input("Enter teacher id"))
                name = input("Enter name")
                mobile = input("Enter mobile")
                email = input("Enter email")
                gender = input("enter gender")
                qualification = input("Enter qualification")
                experience = input("Enter experience")
                sql = "update teacher_management set name=%s,mobile=%s,email=%s,gender=%s,qualification=%s,experience=%s where id=%s"
                values = [name,mobile,email,gender,qualification,experience,teacherid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Teacher details Edited")
                else:
                    print("Error Occured")
            elif TeacherChoice == 3:
                DisplayTeacherDeatils()
                teacherid = int(input("Enter teacher id"))
                sql = "update teacher_management set isDeleted=1 where id=%s"
                values = [teacherid]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Teacher detils Deleted")
                else:
                    print("Error Occured")
            else:
                print("Please eneter the choice between 0-4")
    elif ModuleChoice == 5:
        while 1:
            print("1 for inserting lecture details")
            print("2 for displaying lecture details")
            print("0 for exit")
            LectureChoice = int(input("Enter choice"))
            if LectureChoice == 1:
                print("Below show the details of the teacher")
                DisplayTeacherDeatils()
                print("Below show the deatils of the subject")
                DisplaySubjectDetails()
                print("Below show the details of batch")
                DisplayBatchDetails()
                teacherid = int(input("Enter Teacher id"))
                subjectid = int(input("Enter subject id"))
                batchid = int(input("Enter batch id"))
                duration = input("Enter duration")
                amount = int(input("Enter amount"))
                lecturedate = input("Enter lecture date (YYYY-MM-DD)")
                sql = "insert into lecture_management (teacherid,subjectid,batchid,duration,amount,lecturedate) values (%s,%s,%s,%s,%s,%s)"
                values = [teacherid,subjectid,batchid,duration,amount,lecturedate]
                result = db1.RunQuery(sql,values)
                if result == True:
                    print("Lecture Details Added")
                else:
                    print("Error Occured")
            elif LectureChoice == 0:
                break
            elif LectureChoice == 2:
                sql = "select t.name 'teachername',s.title 'subjectname',b.title 'batchname',l.* from teacher_management t,subject_management s,batch_management b,lecture_management l where t.id=l.teacherid and s.id=l.subjectid and b.id = l.batchid"
                table = db1.FetchRow(sql)
                if table == False:
                    print("Error Occured")
                else:
                    heading = f"{'id':2}|{'Teacher Name':25}|{'Subject Name':25}|{'Batch Name':25}|{'Duration':12}|{'Amount':20}|{'Lecture Date':25}"
                    print(heading)
                    for row in table:
                        row['lecturedate'] = ConvertDatetoDMY(str(row['lecturedate']))
                        print('-'*150)
                        output = f"{row['id']:2}|{row['teachername']:25}|{row['subjectname']:25}|{row['batchname']:25}|{row['duration']:12}|{row['amount']:20}|{row['lecturedate']:25}"
                        print(output)
                print("-"*150)
            else:
                print("Please enter the choice between 0-2")
    elif ModuleChoice==6:
        startdate = input("Enter start date")
        lastdate = input("Enter last date")
        sql = "select t.name 'teachername',s.title 'subjectname',b.title 'batchname',l.* from teacher_management t,subject_management s,batch_management b,lecture_management l where t.id=l.teacherid and s.id=l.subjectid and b.id = l.batchid and l.lecturedate>=%s and l.lecturedate<=%s"
        values = [startdate,lastdate]
        table = db1.FetchRow(sql,values)
        payouttotal =0
        if table == False:
            print("Error Occured")
        else:
            heading = f"{'id':2}|{'Teacher Name':25}|{'Subject Name':25}|{'Batch Name':25}|{'Duration':12}|{'Amount':20}|{'Lecture Date':25}"
            print(heading)
            for row in table:
                payouttotal += row['amount']
                row['lecturedate'] = ConvertDatetoDMY(str(row['lecturedate']))
                print('-'*150)
                output = f"{row['id']:2}|{row['teachername']:25}|{row['subjectname']:25}|{row['batchname']:25}|{row['duration']:12}|{row['amount']:20}|{row['lecturedate']:25}"
                print(output)
        print("-"*150)
        print(f"total Payout {payouttotal}")
        print('_'*150)
    elif ModuleChoice==7:
        while 1:
            print("1 for generate batch wise lecture detail between given date")
            print("2 for  generate batch wise lecture detail with total amount")
            print("0 for exit")
            ReportChoice = int(input("Enter choice"))
            if ReportChoice==1:
                startdate = input("Enter start date")
                lastdate = input("Enter last date")
                sql = "select t.name 'teachername',s.title 'subjectname',b.title 'batchname',b.startdate,b.enddate,l.* from teacher_management t,subject_management s,batch_management b,lecture_management l where t.id=l.teacherid and s.id=l.subjectid and b.id = l.batchid and b.startdate>=%s and b.startdate<=%s"
                values = [startdate,lastdate]
                table = db1.FetchRow(sql,values)
                payouttotal =0
                if table == False:
                    print("Error Occured")
                else:
                    heading = f"{'id':2}|{'Teacher Name':25}|{'Subject Name':25}|{'Batch Name':25}|{'Duration':12}|{'Amount':20}|{'Lecture Date':25}"
                    print(heading)
                    for row in table:
                        payouttotal += row['amount']
                        row['lecturedate'] = ConvertDatetoDMY(str(row['lecturedate']))
                        print('-'*150)
                        output = f"{row['id']:2}|{row['teachername']:25}|{row['subjectname']:25}|{row['batchname']:25}|{row['duration']:12}|{row['amount']:20}|{row['lecturedate']:25}"
                        print(output)
                print("-"*150)
                print(f"total Payout {payouttotal}")
                print('_'*150)
            elif ReportChoice==0:
                break
            elif ReportChoice ==2:
                sql = "select t.name 'teachername',s.title 'subjectname',b.title 'batchname',b.startdate,b.enddate,l.* from teacher_management t,subject_management s,batch_management b,lecture_management l where t.id=l.teacherid and s.id=l.subjectid and b.id = l.batchid"
                table = db1.FetchRow(sql)
                payouttotal =0
                if table == False:
                    print("Error Occured")
                else:
                    heading = f"{'id':2}|{'Teacher Name':25}|{'Subject Name':25}|{'Batch Name':25}|{'Duration':12}|{'Amount':20}|{'Lecture Date':25}"
                    print(heading)
                    for row in table:
                        payouttotal += row['amount']
                        row['lecturedate'] = ConvertDatetoDMY(str(row['lecturedate']))
                        print('-'*150)
                        output = f"{row['id']:2}|{row['teachername']:25}|{row['subjectname']:25}|{row['batchname']:25}|{row['duration']:12}|{row['amount']:20}|{row['lecturedate']:25}"
                        print(output)
                print("-"*150)
                print(f"total Payout {payouttotal}")
                print('_'*150)
            else:
                print("Please enter choice between 0-2")
    elif ModuleChoice==0:
        break



