student={}

while True:
    print("\n -----STUDENT MANAGER APP ----")
    
    print("1. add student")
    print("2. view student")
    print("3. view result ")
    print("4. exit")

    choice = input("Enter your choice :")

    #add student
    if choice  == "1":
        name = input ("Enter student name :")
        marks = int(input("Enter marks :"))
        student[name] = marks
        print(f"{name} successfully added !")

    #view students 
    elif choice == "2":
        if not student:
            print("No students found !")
        else:
            for name ,marks in student.items():
                print(name, ":" , marks)

    #check result
    elif choice =="3":
        name = input("Enter student name :")

        if name in student:
            marks = student [name]

            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

        else :
            print("student not found !")

    #exit
    elif choice =="4":
        print("Exiting...")
        break

    else:
        print("invalid input !")

