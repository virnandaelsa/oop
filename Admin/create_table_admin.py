import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )

    mycursor = mydb.cursor()

    sql = "CREATE TABLE admin(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK INT(12), nama VARCHAR(100),alamat VARCHAR(255), jenkel VARCHAR(55), no_hp INT(12), status VARCHAR(55))"

    mycursor.execute(sql)w