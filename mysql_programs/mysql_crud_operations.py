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
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query)
        if count == 0:
            print("table is created")
        else:
            print("table creation failed")
        cursor.close()
        disconnect_db(connection)
    except:
        print('table creaton error')
create_table()


def create_person_demo():
    query='insert into people (name ,gender, location ,age ) values ("jyothsna",true,"mysore" ,20);'
    try:
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query)
        if count == 0:
            print("table is created")
        else:
            print("table creation failed")
        cursor.close()
        disconnect_db(connection)
    except:
        print('table creaton error')
def read_details():
    name=input("enter person name:")
    gender=input("enter gender:")
    if gender.lower()=='male':
        gender='false'
    else:
        gender='true'
    age=int(input("enter persons age:"))
    location=input("enter person's location:")
    
    return (name,gender,age,location)


def create_person():
    query='insert into people (name ,gender, location ,age ) values (%s,%s,%s,%s);'
    try:
        person=read_person()
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query,person)
        if count == 1:
            print("table is created")
        else:
            print("table creation failed")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print('table creaton error')



def search_person():
    id=int(input("enter the id of the person to be searched:"))
    query=f'select * from people where id ={id}'
    try:        
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query)
        
        if count == 1:
            row = cursor.fetchone()
            print(row)
        else:
            print("no person was found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print('table creaton error')



    
def update_person():
    id=int(input("enter id of the person to be updated:"))
    new_location=input("enter the new location of the person:")
    query='update people set location=%s where id=%s;'
    try:        
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query, (new_location ,id))
        connection.commit()
        cursor.close()
        disconnect_db(connection)
        
        if count == 1:
            print(f'location of person with id {id} is delete updated ')
        else:
            print(f"person with id {id} was not found")
        
    except:
        print('error occoured during updation')
def delete_person():
    id=int(input("enter id to be deleted:"))
    query=f'delete from people where id={id};'
    try:        
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query)
        
        if count == 1:
            print(f'person with is {id} is deleted ')
        else:
            print(f"person with id {id} was not found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print('error occoured during deletion')

def list_people():
    query='select * from people;'
    try:
        connection=connect_db()
        cursor=connection.cursor()
        count= cursor.execute(query)
        if count >= 1:
            rows=cursor.fetchall()
            for row in rows:
                print("row")
        else:
            print("no person found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print('listion people failed')
create_person_demo()
create_person()


def menu():
    print("choice1 = searching the table \n choice2 = updating the table \n choice3 = listing all elements of the table \n choice4 = deleting elements from the table  ")
    choice=int(input("enter your choice of operation"))
    if choice==1:
        search_person()
    elif choice==2:
        update_person()
    elif choice == 3:
        list_people()
    elif choice == 4:
        delete_person()
    else:
        print("please enter a valid choice from the list")
menu()
