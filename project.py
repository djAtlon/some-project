from sqlite3.dbapi2 import SQLITE_CREATE_TABLE, Cursor, connect
import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs



def createConnection(databaseFile):
    connection = None
    try:
        connection = sqlite3.connect(databaseFile)
        return connection
    except Error as error:
        print(error)
    return connection


def createCategoriesTable(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS categories(
                            id int PRIMARY KEY NOT NULL,
                            name text NOT NULL);"""
    
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createProductsTable(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS products(
                            id int PRIMARY KEY NOT NULL,
                            name text NOT NULL,
                            category_id int NOT NULL,
                            FOREIGN KEY (category_id) REFERENCES categories(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)



def insertCategories(connection, category):
    sql_insert_into_table = """INSERT INTO categories VALUES(?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, category)
        connection.commit()
    except Error as error:
        print(error)


def insertProducts(connection, product):
    sql_insert_into_table = """INSERT INTO products VALUES(?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, product)
        connection.commit()
    except Error as error:
        print(error)


def getResponse(url):
    response = requests.get(url)
    return response




def main():
    databaseFile = r'C:\work\tb\uni\project\some-project\database.db'
    connection = createConnection(databaseFile)
    response = getResponse('https://www.foxtrot.com.ua/')
    soup = bs(response.text, 'lxml')
    categories = soup.find_all('li', class_ = 'js-hover-catalog-category')
    phonesAndStuff = [] #телефоны наушники и тд
    laptopsPC = [] #ноутбуки компьютеры планшеты

    response = getResponse('https://www.foxtrot.com.ua/ru/portal-smartfoni-i-telefoni.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    for item in helpArr:
        if item.text.strip() == 'Смартфоны' or item.text.strip() == 'Аксессуары для смартфонов' or item.text.strip() == 'Портативная акустика' or item.text.strip() == 'Наборы для блогеров':
            phonesAndStuff.append(item.text.strip())
    helpArr = []

    response = getResponse('https://www.foxtrot.com.ua/ru/portal-tehnika-dlia-kuhni.html')
    soup = bs(response.text, 'lxml')
    kitchenTechs = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion') #техника для кухни
    
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-tehnika-dlia-doma.html')
    soup = bs(response.text, 'lxml')
    homeTechs = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion') #техника для дома

    response = getResponse('https://www.foxtrot.com.ua/ru/portal-noutbuky-planshety-pk.html') #ноутбуки и планшеты
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    for item in helpArr:
        if item.text.strip() == 'Ноутбуки' or item.text.strip() == 'Планшеты' or item.text.strip() == 'Компьютеры' or item.text.strip() == 'Компьютерная периферия':
            laptopsPC.append(item.text.strip())
    
    
    
    
    print("Start creating tables and insert data into it")
    with connection:
        createCategoriesTable(connection)
        createProductsTable(connection)
        for categoryId, category in enumerate(categories, start=1):
            c = (categoryId, category.text.strip())
            insertCategories(connection, c)
        for phoneAndStuffId, phoneAndStuff in enumerate(phonesAndStuff, start=1):
            p = (phoneAndStuffId, phoneAndStuff, 1)
            insertProducts(connection, p)
        for kitchenId, kitchenTech in enumerate(kitchenTechs, start=5):
            k = (kitchenId, kitchenTech.text.strip(), 2)
            insertProducts(connection, k)
        for homeId, homeTech in enumerate(homeTechs, start=13):
            h = (homeId, homeTech.text.strip(), 3)
            insertProducts(connection, h)
        for laptopPCId, laptopPC in enumerate(laptopsPC, start=21):
            l = (laptopPCId, laptopPC, 4)
            insertProducts(connection, l)
        



if __name__ == '__main__':
    main()