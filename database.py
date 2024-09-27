import sqlite3

create_users_table = "CREATE TABLE IF NOT EXISTS users (username VARCHAR(255) NOT NULL PRIMARY KEY, email TEXT NOT NULL, password TEXT NOT NULL);"

create_admins_table = "CREATE TABLE IF NOT EXISTS admins (username VARCHAR(255) NOT NULL PRIMARY KEY, email TEXT NOT NULL, password TEXT NOT NULL);"


insert_users = "INSERT INTO users (username, email, password) VALUES (?, ?, ?);"

insert_admins = "INSERT INTO admins (username, email, password) VALUES (?, ?, ?);"



get_all_users = "SELECT * FROM users;"

get_all_admins = "SELECT * FROM admins;"


get_user_by_name = "SELECT * FROM users WHERE username = ?; "

get_admin_by_name = "SELECT * FROM admins WHERE username = ?; "


check_user_credentials = "SELECT * FROM users WHERE username = ? AND password = ?;"

check_admin_credentials = "SELECT * FROM admins WHERE username = ? AND password = ?;"

check_username_exists = "SELECT COUNT (*) FROM users WHERE username = ?;"


def connect():
    return sqlite3.connect("login.db")

def create_table(connection):
    with connection:
        connection.execute(create_users_table)

def create_admin_table(connection):
    with connection:
        connection.execute(create_admins_table)



def add_user(connection, username, email, password):
    with connection:
        connection.execute(insert_users, (username, email, password))

def add_admin(connection, username, email, password):
    with connection:
        connection.execute(insert_admins, (username, email, password))



def find_all_users(connection):
    with connection:
        return connection.execute(get_all_users).fetchall()

def find_all_admins(connection):
    with connection:
        return connection.execute(get_all_admins).fetchall()



def find_user_by_name(connection, name):
    with connection:
        return connection.execute(get_user_by_name, (name)).fetchall()

def find_admin_by_name(connection, name):
    with connection:
        return connection.execute(get_admin_by_name, (name)).fetchall()


    
def verify_user(connection, username, password):
    with connection:
        return connection.execute(check_user_credentials, (username, password)).fetchone()

def verify_admin(connection, username, password):
    with connection:
        return connection.execute(check_admin_credentials, (username, password)).fetchone()


def check_user_exists(connection, username):
    with connection:
        result = connection.execute(check_username_exists, (username,)).fetchone()
        return result[0] > 0






# Test the script
conn = connect()
create_table(conn)
create_admin_table(conn)
conn.commit()
#add_admin(conn, "testadmin", "testadmin@example.com", "password")
