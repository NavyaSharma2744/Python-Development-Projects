def registration():
    user_name= input("Enter Your Name: ")
    user_password= input("Enter Your Password: ")
    record ={"uName": user_name, "uCode" :user_password}
    login.append(record)
    print("Registration Successful!")
    print()

def loginuser():
    name= input("Enter Your Name: ")
    password=input("Enter Your Password: ")
    isFound=False
    for i in login:
        if name==i["uName"] and password==i["uCode"]:
            isFound=True
            print("Logged in successfully!")
            break
    if  isFound== False:
        print("Invalid username or password")

login=[]

while True:
    print("1. For Registration")
    print("2. For Login")
    print("3. For Exit")
    val= int(input("Enter Value: "))
    print()

    if val ==1:
        registration()

    elif val == 2:
        loginuser()

    elif val == 3:
        break
    else:
        print()
        print("Invalid Input!")
        print()
        break
