import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM penyewa")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)