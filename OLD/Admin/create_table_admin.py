import mysql.connector

def main():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_py_kelompok"
    )

    mycursor = mydb.cursor()
    try:
        sql = "CREATE TABLE admin(id INT(9) AUTO_INCREMENT PRIMARY KEY, NIK VARCHAR(12), nama VARCHAR(100),alamat VARCHAR(255), jenkel VARCHAR(55), no_hp VARCHAR(12), status VARCHAR(55))"

        mycursor.execute(sql)
    except Exception as e:
        print(e)

main()