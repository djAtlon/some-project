import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs

def createTableMouseBrands(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS mouse_brands(
                            id int PRIMARY KEY NOT NULL,
                            brand_name text UNIQUE NOT NULL,
                            amount int NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertMouseBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO mouse_brands VALUES(?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)



helpArr = []
amount = []
mouseBrandsAndAmount = {}

response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_logitech.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('label', class_ = 'brand')
for item in helpArr:
    print(item.text.strip())
