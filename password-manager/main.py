import random 
import string

password ={}

#load existing password file 
try:
    with open ("password.txt", "r")as file:
        for line in file :
            website, pwd= line.strip().split(":")
            password(website)==password

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits+"!@#$%&"
    password = "".join(random.choice(chars) for _ in range (8))
    return password

while True:
    print("\n----password manager---")
    print("1. save password")
    print("2.view password")
    print("3.generate password ")
    print("4. exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        site = input ("enter website ")
        pwd= input("enter password ")

        password[site] = pwd
        with open ("password.txt", "a") as file :
            file.write(f" {site} : {pwd} \n")
        print("saved ")


    elif choice == "2":
        if not password:
            print("No password found ")

        else :
            for site ,pwd in password.items():
                print(site, ":" ,pwd)

    elif choice == "3":
        print("generated password " , generate_password())

    elif choice =="4":
        print("ok bye")
        break

    else:
        print(" IN valid input ")


        