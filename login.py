import database
import welcomeUser
import welcomeAdmin

# menu_prompt = """ -------------------- LOGIN  PAGE --------------------------
# PLEASE CHOOSE ONE OF THE OPTIONS BELOW
# 1) LOGIN
# 2) SIGN UP
# 3) EXIT

# YOUR SELECTION(1-3): """

# def menu():
#     connection = database.connect()
#     database.create_table(connection) 
    
#     while (user_input := input(menu_prompt)) !="3":
#         if user_input == "1":
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             user = database.verify_user(connection, username, password)
#             if user:
#                 print(f"Welcome back, {username}!")
#             else:
#                 print("Invalid username or password. Please try again.")


#         elif user_input == "2":
#             username = input("Enter your username: ")
#             email = input("Enter your email: ")
#             password = input("Enter your password: ")
            
#             database.add_user(connection, username, email, password)
#         else:
#             print("INVALID SELECTION. PLEASE TRY AGAIN.")


# menu()
def login(connection):
    
    print("HOW WOULD YOU WISH TO LOG INTO THE PROGRAM AS; ")
    print("1. USER")
    print("2. ADMIN")
    choice_one = input("Your choice: ")
    
    if choice_one == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        user = database.verify_user(connection, username, password)
        
        if user:
            print(f"Welcome back, {username}!")
            welcomeUser.welcome_user()
        else:
            print("Invalid username or password. Please try again.")
    elif choice_one == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        user = database.verify_admin(connection, username, password)
        
        if user:
            print(f"Welcome back, {username}!")
            welcomeAdmin.welcome_admin()
    else:
        print("INVALID SELECTION. PLEASE TRY AGAIN.")

def signup(connection):
    
    print("HOW WOULD YOU WISH TO CREATE YOUR ACCOUNT IN THE PROGRAM AS; ")
    print("1. USER")
    print("2. ADMIN")
    choice_two = input("Your choice: ")
    
    if choice_two == "1":
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
            
        database.add_user(connection, username, email, password)
    elif choice_two == "2":
        print("Admin login coming soon")
    else:
        print("INVALID SELECTION. PLEASE TRY AGAIN.")

    
    
    
def main():
    connection = database.connect()
    database.create_table(connection)
    database.create_admin_table(connection)
    
    print("------------------------------------------LOGIN PAGE----------------------------------------------")
    print("PLEASE CHOOSE ONE OF THE OPTIONS BELOW.")
    print("\t1. LOGIN")
    print("\t2. SIGN UP")
    print("\t3. EXIT")

    choice = input("Your selection: ")

    is_running = True

    while is_running:
        if choice == "1":
            login(connection)
        elif choice == "2":
            signup(connection)
        elif choice == "3":
            is_running = False
        else:
            print("INVALID SELECTION. PLEASE TRY AGAIN.")
            
        
        connection.close()

if __name__ == "__main__":
    main()


