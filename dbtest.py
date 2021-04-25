import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                        port = '3306',
                        user='root',
                        password='viku@54321',
                        database='pythontest')
        query = 'create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    #insert
    def insert_user(self,userId,userName,phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(userId,userName,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user save to db")

    #fetch all
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userId:",row[0])
            print("userName:",row[1])
            print("phone:",row[2])
            print()

    def fetch_one(self):
        query="select userId from user "
        cur = self.con.cursor()
        cur.execute(query)
        for r in cur:
            print("userId:",r)
            print()

    #delete user
    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")


        

helper = DBHelper()
helper.delete_user(25)
helper.fetch_all()
# helper.insert_user(152,'dar',"2344")
# helper.insert_user(234,'deepak',"234433")
# helper.insert_user(125,'rahul',"234422")
# helper.insert_user(25,'jhaji',"1122344")
# helper.insert_user(1125,'luv',"122344")
# import sqlalchemy
# # from sqlalchemy import cursor,create_engine

# class DBHelper:
#     def __init__(self):
#         self.engine=sqlalchemy.create_engine('mysql+pymysql://root:viku@54321@localhost:3306/pythontest')
#         # engine = sqlalchemy.create_engine('mysql+pymysql://root:viku@54321@localhost:3306/pythontest')
#         query='create table if not exists user2(userId int primary key,userName varchar(200),phone varchar(12))'

#         conn = self.engine.connect()
#         conn.execute(query)
#         # cur = self.engine.cursor()
#         # execute(self.engine,query)
#         print("Created")

# helper = DBHelper()


