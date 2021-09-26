from sqlite3.dbapi2 import Cursor, connect
from requests.models import cookiejar_from_dict
import telebot
import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as error:
        print(error)
    return connection

def create_table_categories(connection):
    sql_create_table = """ CREATE TABLE IF NOT EXISTS categories(
                            id int PRIMARY KEY NOT NULL,
                            category_name text NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def create_table_products(connection):
    sql_create_table = """ CREATE TABLE IF NOT EXISTS products(
                            id int PRIMARY KEY NOT NULL,
                            product_name text NOT NULL,
                            category_id int NOT NULL,
                            FOREIGN KEY (category_id) REFERENCES categories (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def create_table_laptop(connection):
    sql_create_table = """ CREATE TABLE IF NOT EXISTS laptop(
                            laptop_id int PRIMARY KEY NOT NULL,
                            mark_name text NOT NULL,
                            product_id int NOT NULL,
                            amount int NOT NULL,
                            FOREIGN KEY (product_id) REFERENCES products (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def insert_into_table_categories(connection, category):
    sql_insert_into_table = """ INSERT INTO categories VALUES(?, ?);"""
    cursor = connection.cursor()
    cursor.execute(sql_insert_into_table, category)
    connection.commit()
    return cursor.lastrowid



def insert_into_table_product(connection, product):
    sql_insert_into_table = """ INSERT INTO products VALUES(?, ?, ?);"""
    cursor = connection.cursor()
    cursor.execute(sql_insert_into_table, product)
    connection.commit()
    return cursor.lastrowid



def main():
    categoryId = 1
    productId = 1 
    database = r'C:\stuff\uni_course 4\pythonStuff\project\database.db'
    main_url = 'https://rozetka.com.ua/'
    laptop_and_pc_url = 'https://rozetka.com.ua/computers-notebooks/c80253/'
    phones_and_TVs_url = 'https://rozetka.com.ua/telefony-tv-i-ehlektronika/c4627949/'
    gaming_url = 'https://rozetka.com.ua/game-zone/c80261/'
    laptop_url = 'https://rozetka.com.ua/notebooks/c80004/'

    response = requests.get(main_url)
    soup = bs(response.text, 'lxml')
    categories = soup.find_all('span', class_ = 'main-categories__link-text')

    response = requests.get(laptop_and_pc_url)
    soup = bs(response.text, 'lxml')
    productsLaptopPC = soup.find_all('a', class_ = 'tile-cats__heading tile-cats__heading_type_center ng-star-inserted')

    response = requests.get(phones_and_TVs_url)
    soup = bs(response.text, 'lxml')
    productsPhonesTVs = soup.find_all('a', class_ = 'tile-cats__heading tile-cats__heading_type_center ng-star-inserted')

    response = requests.get(gaming_url)
    soup = bs(response.text, 'lxml')
    gaming = soup.find_all('a', class_ = 'tile-cats__heading tile-cats__heading_type_center ng-star-inserted')

    response = requests.get(laptop_url)
    soup = bs(response.text, 'lxml')
    laptops = []
    while len(laptops) != 15:
        laptops = soup.find_all('label')
    for l in laptops:
        print(l)

    
    connection = create_connection(database)
    
    # CREATING TABLE CATEGIRIES AND PRODUCTS AND INTO IT
    # with connection:
    #     create_table_categories(connection)
    #     create_table_products(connection)
    #     create_table_laptop(connection)
    # with connection:
    #     for c in categories:
    #         category = (categoryId, c.text)
    #         category_id = insert_into_table_categories(connection, category)
    #         categoryId += 1
    #     for p in productsLaptopPC:
    #         product = (productId, p.text, 1)
    #         productLaptopPC_id = insert_into_table_product(connection, product)
    #         productId += 1
    #     for p in productsPhonesTVs:
    #         product = (productId, p.text, 2)
    #         productPhoneTVs_id = insert_into_table_product(connection, product)
    #         productId += 1
    #     for g in gaming:
    #         product = (productId, g.text, 3)
    #         gaming_id = insert_into_table_product(connection, product)
    #         productId += 1
        
            
    #--------------------------------------------

if __name__ == '__main__':
    main()