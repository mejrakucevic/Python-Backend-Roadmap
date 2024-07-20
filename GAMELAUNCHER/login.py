


def createAccount():
    username = input("Input your username: ")
    password = input("Input your password: ")
    print("User " + username + " created successfully")
    
    print("Log in now: ")
    username1 = input("Input your username: ")
    password1 = input("Input your password: ")
    
    if (username1 == username and password == password1):
        print("Logged in sucessfully")
    else: print("Wrong password or username!")
    
    while (username1 != username or password != password1):
         print("Log in now: ")
         username1 = input("Input your username: ")
         password1 = input("Input your password: ")
        
    
    print("User logged in sucessfully")
    

createAccount()