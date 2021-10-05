from sqlite3.dbapi2 import Cursor
import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs

def createComputerProducts(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS computer_products(
                            id int PRIMARY KEY NOT NULL,
                            name text UNIQUE NOT NULL,
                            product_id int NOT NULL,
                            FOREIGN KEY (product_id) REFERENCES products (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertComputerProducts(connection, product):
    sql_insert_into_table = """INSERT INTO computer_products VALUES (?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, product)
        connection.commit()
    except Error as error:
        print(error)

mainUrl = 'https://www.foxtrot.com.ua/'
product_names = []
response = requests.get('https://www.foxtrot.com.ua/ru/portal-komputernaya-pereferiya.html')
soup = bs(response.text, 'lxml')
divs = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion-portal2')
for div in divs:
    links = div.find_all('a')
    for link in links:
        product_names.append(link.text.strip())