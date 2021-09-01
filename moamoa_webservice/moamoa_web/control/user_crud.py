from flask_login import UserMixin
from database.mysql import conn_mysqldb

class User(UserMixin):

    def __init__(self,user_id,user_email,user_name,user_location,user_product):
        self.id=user_id
        self.user_name = user_name
        self.user_email=user_email
        self.user_location=user_location
        self.user_product=user_product
    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        mysql_db=conn_mysqldb()
        db_cursor=mysql_db.cursor()
        sql="SELECT * FROM moa_info WHERE USER_ID = '" +str(user_id) + "'"

        db_cursor.execute(sql)
        user=db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id=user[0],user_name=user[1],user_email=user[2],user_location=user[3],user_product=user[4])
        return user

    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM moa_info WHERE USER_EMAIL = '" + \
            str(user_email) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            db_cursor.close()
            return None
        user = User(user_id=user[0],user_name=user[1],user_email=user[2],user_location=user[3],user_product=user[4])
        db_cursor.close()
        return user

    @staticmethod
    def create(user_name,user_email,user_location,user_product):
        user = User.find(user_email)
        if user == None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO moa_info (USER_NAME,USER_EMAIL,USER_LOCATION,USER_PRODUCT) VALUES ('%s', '%s', '%s','%s')" % (
                str(user_name), str(user_email),str(user_location),str(user_product))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user

    @staticmethod
    def delete(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM moa_info WHERE USER_ID = %d" % (user_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted

    @staticmethod
    def all_email():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT USER_EMAIL from moa_info"
        db_cursor.execute(sql)
        email= db_cursor.fetchall()
        return email
    
    @staticmethod
    def get_location(email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT USER_LOCATION FROM moa_info WHERE USER_EMAIL = '" + \
        str(email) + "'"
        db_cursor.execute(sql)
        location= db_cursor.fetchone()
        return location 

    # 예측값 집어넣기
    @staticmethod
    def product(name,today_predict,today_trade,tommorow_predict,tommorow_trade,toto_predict,toto_trade,next_predict,next_trade):
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO predict_info (product_name,today_predict,today_trade,tommorow_predict,tommorow_trade,toto_predict,toto_trade,next_predict,next_trade) VALUES ('%s', '%s', '%s','%s','%s', '%s', '%s','%s','%s')" % (
                str(name), str(today_predict),str(today_trade),str(tommorow_predict),str(tommorow_trade),str(toto_predict),str(toto_trade),str(next_predict),str(next_trade))
            db_cursor.execute(sql)
            mysql_db.commit()

    #예측값 품종이름으로 가져오기
    @staticmethod
    def predict(product):
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "SELECT * FROM predict_info WHERE product_name = '" + \
            str(product) + "'"
            db_cursor.execute(sql)
            product_list= db_cursor.fetchall()
            return product_list

    #email로 품종가져오기
    @staticmethod
    def get_product(email):
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "SELECT USER_PRODUCT FROM moa_info WHERE USER_EMAIL = '" + \
            str(email) + "'"
            db_cursor.execute(sql)
            product= db_cursor.fetchone()
            return product
    @staticmethod
    def truncate():
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "truncate predict_info"
            db_cursor.execute(sql)