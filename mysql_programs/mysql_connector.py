import pymysql


def connect_db():
    try:
        connection=pymysql.connect(user="root",password="root",port=3306,database="whataever",charset='utf8', host='localhost')
        print('db connected')
        return connection
    except:
        print("db connection failed")
def disconnect_db():
    try:
        connection.close()
        print("db disconnected")
    except:
        print("db disconnection failed")
def create_table(connection):
    query= 'create table IF NOT EXISTS people(id int primary key auto_increment, name varchar(50) not null,gender bool not null, age int default(0), location varchar(50));'
    try:
        connection=connect_db
        cursor=connection.cursor()
        count= cursor.execute(query)
        if count == 0:
            print("table is created")
        else:
            print("table creation failed")
        cursor.close()
        disconnect_db()
    except:
        print('table creation error')
create_table()
