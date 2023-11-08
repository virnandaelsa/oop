import mysql.connector
from sys import path
path.append("C:\\Users\\ACER\\Documents\\pbl\\Admin")

import Admin.Admin

class Penyewa(Admin):
    def __init__(self):
        super().__init__()

    def update_data(self, nik, name, alamat, jk, hp, sts):
        if sts == "penyewa":
            super().update_data(nik, name, alamat, jk, hp, sts)
    
    

