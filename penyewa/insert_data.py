import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)
sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
val = ("Aldo", "aldo", "aldo000", "Admin")