import re
import time
import os
import datetime

 
from datetime import date, datetime




def editingDescription(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    newDes = input("Enter Your New Description : ")
                    project_info[2] = newDes
                    finalInfor = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                         
                        print(f"Your new description [{newDes}] is successfully added\n")
                        flag = 1
                else:
                    project_info = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
        print(f"We can not found a title with this name [{projectTitle}]")
 

    os.rename("/home/hanan/Desktop/ITI_Python_project/temp.txt", "/home/hanan/Desktop/ITI_Python_project/projects.txt")



def editingTitle(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    
    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    while True:
                        newTitle = input("Enter the new title : ")
                        if newTitle.isalnum():
                            newTitle = str(newTitle)
                            break
                        else:
                            print("Invalid naming of a title, Try again")
                    project_info[1] = newTitle
                    finalInfor = ":".join(project_info)
                
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                         
                        print(f"Your New Title [{newTitle}] is Successfully added, You will back to Menu")
                        
                        flag = 1
                else:
                    project_info = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
        print(f"We can not found a title with this name [{projectTitle}]")
 
    os.rename("/home/hanan/Desktop/ITI_Python_project/temp.txt", "/home/hanan/Desktop/ITI_Python_project/projects.txt")

    

def editingTotalTarget(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    while True:
                        newTotal = input("Enter your new total target : ")
                        if newTotal.isnumeric():
                            newTotal = str(newTotal)
                            break
                        else:
                            print("Invalid type of a total target, try again")
                    project_info[3] = newTotal
                    finalInfor = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        editingFile.writelines(data)
                         
                        print(f"Your new total target [{newTotal}] is successfully added \n")
                        flag = 1
                else:
                    project_info = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
        print(f"We can not found a title with this name [{projectTitle}]")
 
    os.rename("/home/hanan/Desktop/ITI_Python_project/temp.txt", "/home/hanan/Desktop/ITI_Python_project/projects.txt")

def editEndDate(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0

    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                        print ("Enter your new start date \n")

                        year=int(input("year : "))
                        month=int(input("month :"))
                        day=int(input("day :"))
                        newDate=str(date(year,month,day))

                        project_info[5] = newDate
                        finalInfor = ":".join(project_info)
                    
                        with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as editingFile:
                            data = finalInfor.strip("\n")
                            data = f"{data}\n"
                            editingFile.writelines(data)
                            print(f"Your New Date [{newDate}] is Successfully added")
                            
                            flag = 1
                        break
                else:
                    project_info = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
         print(f"We can not found a title with this name [{projectTitle}]")
  
    os.rename("/home/hanan/Desktop/ITI_Python_project/temp.txt", "/home/hanan/Desktop/ITI_Python_project/projects.txt")
 

def editStartDate(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0

    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                        print("Enter Your New Start Date  ")
                        year=int(input("Enter the new year : "))
                        month=int(input("month : "))
                        day=int(input("day : "))
                        newDate=str(date(year,month,day))
                    
                        
                        project_info[4] = newDate
                        finalInfor = ":".join(project_info)
                    
                        with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as editingFile:
                            data = finalInfor.strip("\n")
                            data = f"{data}\n"
                            editingFile.writelines(data)
                            print(f"Your New Date [{newDate}] is Successfully added")
                            
                            flag = 1
                        break
                else:
                    project_info = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
         print(f"We can not found a title with this name [{projectTitle}]")
  
    os.rename("/home/hanan/Desktop/ITI_Python_project/temp.txt", "/home/hanan/Desktop/ITI_Python_project/projects.txt")



def Searching(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    
    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    print(f"User email: {project_info[0]}\n")
                    print(f"Project title: {project_info[1]}\n")
                    print(f"Description: {project_info[2]}\n")
                    print(f"Total target: {project_info[3]}\n")
                    print(f"Start date: {project_info[4]}\n")
                    print(f"End date: {project_info[5]}\n")
                    flag = 1

    if flag == 0:
         print(f"We can not found a project  with this name [{projectTitle}]")





def editing(usermail,title):

    
    print("\n")
    print("1.Edit title" )
    print("2.Edit Description" )
    print("3.Edit total target" )
    print("4.Edit start date" )
    print("5.Edit end date" )
    choise= int(input("please enter your choise : " ))

    if choise ==1 :
        editingTitle(usermail, title)        
    elif choise == 2:
        editingDescription(usermail, title)
 
    elif choise == 3:
        editingTotalTarget(usermail, title)

    elif choise == 4:
        editStartDate(usermail, title)
      
    elif choise == 5:
        editEndDate(usermail, title)
      
    else:
            print("please enter valid number")
            editing()
       



def createProject(email):
    title = input("Enter title : ")
    details = input("Project Details: ")
    totalTarget =input("total target: ")
    print("start date")
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    start_date =str(date(year, month, day))

    print("End date")
    year1 = int(input('Enter a year: '))
    month1 = int(input('Enter a month: '))
    day1 = int(input('Enter a day: '))
    end_date =str(date(year1, month1, day1))

    project_data = [email, title, details, totalTarget, start_date, end_date]
    finalInfor = ":".join(project_data)
    with open(f"/home/hanan/Desktop/ITI_Python_project/projects.txt", "a") as projectFile:
        data = finalInfor.strip("\n")
        data = f"{data}\n"
        projectFile.write(data)
         
        
        print("project added Successfully"+"\n")
         
     

def delete_Project(usermail, title):
    projectTitle = title
    email = usermail
    flag = 0
    
    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if email == project_info[0]:
                if projectTitle == project_info[1]:
                    finalInfor = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as editingFile:
                        data = finalInfor.strip("\n")
                        data = f"{data}\n"
                        if not (email == project_info[0] and projectTitle == project_info[1]):
                            editingFile.writelines(data)
                            flag = 0
                        else:
                            print("The project has been deleted successfully ")
                            flag = 1
                else:
                    project_info = ":".join(project_info)
                    with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                        data = project_info.strip("\n")
                        data = f"{data}\n"
                        notEditingFile.writelines(data)

            else:
                project_info = ":".join(project_info)
                with open("/home/hanan/Desktop/ITI_Python_project/temp.txt", "a") as notEditingFile:
                    data = project_info.strip("\n")
                    data = f"{data}\n"
                    notEditingFile.writelines(data)

    if flag == 0:
         print(f"We can not found a title with this name [{projectTitle}]")

    os.rename("/home/hanan/Desktop/ITI_Python_project/temp.txt", "/home/hanan/Desktop/ITI_Python_project/projects.txt")



 
def viewProjects(email):
    userMail = email
    flag = 0
    with open("/home/hanan/Desktop/ITI_Python_project/projects.txt") as readFile:
        projects = readFile.readlines()
        counter = 1
        for project in projects:
            project = project.strip("\n")
            project_info = project.split(":")
            if project_info == [""]:
                flag = 0
            else:
                if userMail == project_info[0]:
                    print(f"Project {counter} ")
                    print(f"User Email: {project_info[0]}")
                    print(f"Project title: {project_info[1]}")
                    print(f"Description: {project_info[2]}")
                    print(f"Total target: {project_info[3]}")
                    print(f"Start Date: {project_info[4]}")
                    print(f"End Date: {project_info[5]}\n")
                    counter += 1
                    flag = 1

    if flag == 0:
        print(" You donot have any Projects Yet \n ")
              
    
 

def projects_menu(email):
    while True:
        print("projects menue")
        print("1.Create project")
        print("2.Search")
        print("3.Delete")
        print("4.Edit") 
        print("5.View all projects")
        print("6.Return to the login menue ")
        print("7.Exit")
        print("\n")
        choise= int(input("please enter your choise : " ))
        print("\n")

        if choise ==1 :
            createProject(email )
        elif choise == 2:
             title=input("Enter the project title : ")
             Searching(email ,title) 
        elif choise == 3:
            title=input("Enter the project title : ")

            delete_Project(email,title )
        elif choise == 4:
            title=input("Enter the project title : ")

            editing( email,title)       
        elif choise == 5:
            viewProjects(email )
        elif choise ==6:
            login()   
        elif choise ==7:
            break    
        else:
            print("please enter valid number")
       


def signup():
    name=input("please enter your full name name : ").strip()
    id=round(time.time())
    name_id=f"{id}:{name}"
    phone=input("please enter your phone : ").strip()
    r=re.fullmatch('[010][0-9]{10}',phone)  
    r1=re.fullmatch('[011][0-9]{10}',phone)  
    r2=re.fullmatch('[012][0-9]{10}',phone)  

    if r ==None or r1==None or r2==None:  
         print('Not egyptian  valid number'+"\n")
         signup()   
    else :
        pass
    email = input("Enter email address: ").strip()
    if "@"  in email and ".com" in email :
        pass
    else:
        print("please enter valid email format"+"\n")
        signup()
       
    pwd =str(input("Enter password: ")).strip()
    
    conf_pwd = input("Confirm password: ").strip()
    if conf_pwd == pwd:
        pass

        with open("/home/hanan/Desktop/ITI_Python_project/credentials.txt", "a") as f:
            userdata= [name_id,phone,email ,pwd]

            userdata = ":".join(userdata)
            f.write(userdata+"\n")
                
        f.close()
        print("\n"+"You have registered successfully"+"\n")

    else:
        print(" confirm password is not same password  \n")

        system()   


def projects()  :    
    if login()==True:
        pass
    projects_menu()
    

def checklogin(email, password):
    with open("/home/hanan/Desktop/ITI_Python_project/credentials.txt") as readFile:
        users = readFile.readlines()
        for user in users:
            user = user.strip("\n")
            user_info = user.split(":")
            if user_info[3] == email and user_info[4] == password:
                return True
    return False

def login():
    Email = input("Enter Your Email:").strip()
    Password = input("Enter Your Password:").strip()
    if checklogin(Email, Password):
        print("\nLoging Successfully\n")
        projects_menu(Email)
        return True
    else:
        print("Invalid username or Email ,Please Try again")
        return login()


def system () :       
    while 1:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        num =int(input("Enter your choice: "))
        if num == 1:
            signup()
        elif num == 2:
            login()
            break
        elif num == 3:
            break
        else:
            print("Wrong Choice!")


system() 