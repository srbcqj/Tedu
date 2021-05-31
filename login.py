"""
mysql 操作流程演示
"""

import pymysql

class Databases:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user="root",
                             password='123456',
                             database='stu',
                             charset='utf8'
                             )
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def register(self,name,password):
        sql = "select * from user where name = %s;"
        self.cur.execute(sql,[name])
        data = self.cur.fetchone()
        if data :
            return False

        try:
            sql = "insert into user(name,password) values(%s,%s)"
            self.cur.execute(sql,[name,password])
            self.db.commit()
            return True
        except :
            self.db.rollback()
            return False

    def login(self,name,password):
        try:
            sql = "select * from user where name = %s;"
            self.cur.execute(sql,[name])
            self.db.commit()
            data = self.cur.fetchone()
            if data[3] == password:
                return True
            else:
                return False
        except :
            return False


if __name__ == '__main__':
    db = Databases()
    # db.register('Tom',123456)
    db.login('Tom',123456)
    db.close()
    
print("哈哈")
print("哈哈哈")
“修改”
