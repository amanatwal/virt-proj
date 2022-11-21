"""
Application Name: Lab03_Amandeep_Kaur.py
Programmer Name: Amandeep Kaur
Student Id: N01261681
Description: This application enrolls a student in course and adds information about test mark1 and test mark2 in the course.
It also calculates the average of the two tests for each student enrolled in the course.
Change trial
"""

# import statistics
def author_info():
    name="%120s" % "Amandeep Kaur"
    student_ID="%120s\n"%"N01261681"
    print(name)
    print(student_ID)
    
def add_student(student_info):   # Adding the student information and calculating the average of entered marks
    first_name=input("Enter First Name:\t")
    last_name=input("Enter Last Name:\t")
    student_number=input("Enter Student Number\t")
    test_mark1=int(input("Enter Mark 1:\t"))
    test_mark2=int(input("Enter Mark 2\t"))
    average = float((test_mark1 + test_mark2)/2)
  
    
    data=""
    if student_info=="":
        
        print("There is no student in the system, yet!")
        print("Adding students to records")
        data += first_name + ',' + last_name + ',' + student_number + ',' + str(test_mark1) + ',' + str(test_mark2) + ',' +str(("%.2f") % (average))
        student_info += data
        return student_info
    else: # student_info has data
        student_exists=False
        each_student_info=student_info.split(';')
        for student in each_student_info:
            student_details=student.split(',')
            if student_number == student_details[2]:
                print("Student is already registered.. \nStudent No. is in records\n\n")
                student_exists = True
                break
        if student_exists == False:
            print("Student information is saved to the records\n")
            data += first_name + ',' + last_name + ',' + student_number + ',' + str(test_mark1) + ',' + str(test_mark2) + ',' + str(("%.2f") % (average))
            student_info += ';' + data
            return student_info
        else:
            print("Student is already existing in records")

        return student_info
def display_students(student_info):
    if student_info == "":
        print("Sorry ! There is no record of any student to display")
    else:
        print("Student(s) information is displayed below\n\n")
        author_info()
        display_students=""
        header="%20s%20s%20s%20s%20s%20s\n"%("First Name", "Last Name", "Student Number", "Test Mark 1", "Test Mark2", "Average")
        display_students+=header
        each_student_info=student_info.split(';')
        for student in each_student_info:
            student_details=student.split(',')
            display="%20s%20s%20s%20s%20s%20s\n"%(student_details[0], student_details[1], student_details[2],student_details[3],student_details[4], student_details[5])
            display_students+=display

        print(display_students)
def my_menu():
    menu = """
    1.  Add student information
    2.  Display all students
    3.  Search students by student number
    4.  End application
    """
    print(menu)
    mychoice = input("Enter your choice:\t")
    return mychoice

def student_search_by_student_number(student_info):
    
    if student_info == "":
        print("There is no student in the records...\n")
        return
    else:
        search_student_number_info=input("Enter Student No. to search student\t\t")
        # author_info()
        display_students=""
        header="%20s%20s%20s%20s%20s%20s\n"%("First Name", "Last Name", "Student Number", "Test Mark 1", "Test Mark2", "Average")
        display_students+=header
        student_exists = False
        student_details_found=""
        each_student_info = student_info.split(';')
        for student in each_student_info:
            student_details = student.split(',')
            if search_student_number_info == student_details[2]:
                
                print("Student is registered \nStudent information is given below\n\n")
                student_exists = True
                student_details_found="%20s%20s%20s%20s%20s%20s\n"%(student_details[0], student_details[1], student_details[2],student_details[3],student_details[4], student_details[5])
                display_students+=student_details_found
                author_info()
                print(display_students)
                
                break

        if student_exists == False:
            print("This Student is NOT in the records")

    return
    
        
def main():
    student_info=""
    while True:
        #author_info()
        choice=my_menu()
        if choice == '1':
            student_info=add_student(student_info)
        elif choice == '2':
            display_students(student_info)
        elif choice == '3':
            student_search_by_student_number(student_info)
        elif choice == '4':
            print("Application Ending Now ! \nGood Bye ! ")
            break
        else:
            print("Enter valid choice and continue application...")
            
    
main()   
