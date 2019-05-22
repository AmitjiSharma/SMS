import sqlite3
class Student:
    def __init__(self):
        print('''
                 -----------------------------------------------------------------------
                 |                                                                     |
                 |                **********************************                   |                                         |
                 |----------------* Global Institute Of Technology *-------------------|                        
                 |                **********************************                   |
                 |                                                                     |                 
                 |---------------------------------------------------------------------|                                                                     |                        
        ''')

        print("------------------------------------------------------------------------------------------------------------------------------------------")
        Login_Option=int(input("1.Admin Login \n2.Student Login\n3.Visitor Login\n"))
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        if Login_Option==1:
            self.Admin_Login()
        elif Login_Option==2:
            Student_Login()
        elif Login_Option==3:
            Visitor()
    #Function For Admin Login:-
    def Admin_Login(self):
        Username=input("Enter Username:-\n")
        Password=input("Enter Password:-\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------")
        if Username=='Amit' and Password=="India":

            Admin_Option=int(input("1.Add New Student Details\n2.Remove Existing Student Details\n3.Send Report to Parents\n4.Show All Student Details\n"))
            #For Adding Students detail:-
            print("------------------------------------------------------------------------------------------------------------------------------------------")
            if Admin_Option==1:
                C=sqlite3.connect('Information.db')
                C.execute('CREATE TABLE IF NOT EXISTS Student_Data(Name text,Age int,Mail text,Contact text,HSE int,SSE int,Address text,Father_Mail text,Father_Contact text,Father_Name)')
                #Number_of_Students=int(input("How many student's data you want to insert:-\n"))
                #for i in range(1,Number_of_Students+1):
                Name=input(f"Enter name of student :-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Age=int(input(f"Enter Age of {Name}:-\n"))
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Mail=input(f"Enter E-mail address of {Name}'s:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Contact=input(f"Enter contact number of {Name}'s:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                HSE=int(input(f"Enter 10th percentage of {Name}'s:-\n"))
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                SSE=int(input(f"Enter 12th percentage of {Name}'s:-\n"))
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Address=input(f"Enter {Name}'s permanent address:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Father_Mail=input(f"Enter {Name}'s Father's E-mail address:-\n ")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Father_Contact=input(f"Enter {Name}'s Father's Contact Number\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                Father_Name=input(f"Enter {Name}'s Father's name:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                C.execute('INSERT INTO Student_Data(Name,Age,Mail,Contact,HSE,SSE,Address,Father_Mail,Father_Contact,Father_Name) values(?,?,?,?,?,?,?,?,?,?)',(Name,Age,Mail,Contact,HSE,SSE,Address,Father_Mail,Father_Contact,Father_Name))
                print("Student data inserted successfully:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                C.commit()
            #For Removing Students Details:-
            if Admin_Option==2:
                C=sqlite3.Connection('Information.db')
                Name=input("Enter Name of Student Whose record you want to delete from the database:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                fName=input(f"Enter {Name}'s Father's name:-\n")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                C.execute(f'DELETE from Student_Data where Name=Name and Father_Name=Father_Name')
                print(f"{Name}'s record is successfully deleted")
                print("------------------------------------------------------------------------------------------------------------------------------------------")
                C.commit()

Student_Object = Student()
