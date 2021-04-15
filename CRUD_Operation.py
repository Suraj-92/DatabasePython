'''
Author: Suraj N Temkar
Date: 15/04/2021
Title: Perform CRUD Operations 
'''

import mysql.connector as connector
import logging
import Logger1

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formater = logging.Formatter('%(levelname)s : %(message)s')

file_handler = logging.FileHandler('database.log')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)


class CRUD:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='root',database='pythontest')

        query = 'create table if not exists student(studentId int primary key, studentName varchar(200),phone varchar(12))'

        cur = self.con.cursor()

        cur.execute(query)

        print("Created....")

    # insert 
    def insert(self,studentId, studentName, phone):
        query = "insert into student(studentId,studentName,phone) values ({},'{}','{}')".format(studentId,studentName,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data inserted on DB Successfully...")

    # Select
    def select(self):
        query = "select *from student"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("studentId : ",row[0])
            print("studentName : ",row[1])
            print("Phone : ",row[2])

    # Delete Query
    def delete(self,studentId):
        query = "delete from student where studentId = {}".format(studentId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Deleted Successfully....")

    # Update Query
    def update(self,studentId,newName,newPhone):
        query = "update student set studentName = '{}', phone = '{}' where studentId = {}".format(newName,newPhone,studentId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Updated Successfully...")


# if __name__ == '__main__':
#     operations = CRUD()
#     # operations.insert(21,"Suraj","8668958393")
#     # operations.insert(204,"Raj","4578421578")
#     # operations.insert(80,"Soham","9578461254")
#     # operations.select()
#     operations.delete(80)
#     operations.select()
#     operations.update(204,"Anjali","5784578457")
#     operations.select()
