from sqlite3 import Error

def createSamsungPhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS samsung_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createApplePhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS apple_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createXiaomiPhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS xiaomi_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createOppoPhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS oppo_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createHuaweiPhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS huawei_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createMeizuPhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS meizu_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)



def createOneplusPhone(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS oneplus_phone(
                            id int PRIMARY KEY NOT NULL,
                            phone_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES phone_brands(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def insertSamsungPhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO samsung_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)

def insertApplePhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO apple_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)

def insertXiaomiPhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO xiaomi_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)

def insertOppoPhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO oppo_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)

def insertHuaweiPhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO huawei_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)

def insertMeizuPhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO meizu_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)


def insertOneplusPhones(connection, insertPhone):
    sql_insert_into_table = """INSERT INTO oneplus_phone VALUES(?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, insertPhone)
        connection.commit()
    except Error as error:
        print(error)