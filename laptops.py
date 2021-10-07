#25
import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs


def returnPrice(helpArr):
    priceArr = []
    for item in helpArr:
        price = item.text.strip()
        new_price = price.split('₴')[0]
        firstPart = new_price.split(' ')[0]
        secondPart = new_price.split(' ')[1]
        priceArr.append(int(firstPart + secondPart))
    return priceArr



def createLaptopsBrands(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS laptop_brands(
                            id int PRIMARY KEY NOT NULL,
                            brand_name text UNIQUE NOT NULL,
                            amount int NOT NULL,
                            product_id int NOT NULL,
                            FOREIGN KEY (product_id) REFERENCES products (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createLenovoLaptop(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS lenovo_laptop(
                            id int PRIMARY KEY NOT NULL,
                            laptop_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES laptop_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAsusLaptop(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS asus_laptop(
                            id int PRIMARY KEY NOT NULL,
                            laptop_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES laptop_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAcerLaptop(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS acer_laptop(
                            id int PRIMARY KEY NOT NULL,
                            laptop_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES laptop_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAppleLaptop(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS apple_laptop(
                            id int PRIMARY KEY NOT NULL,
                            laptop_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES laptop_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createHpLaptop(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS hp_laptop(
                            id int PRIMARY KEY NOT NULL,
                            laptop_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES laptop_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createDellLaptop(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS dell_laptop(
                            id int PRIMARY KEY NOT NULL,
                            laptop_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES laptop_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertLaptopBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO laptop_brands VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)

def insertLenovoLaptop(connection, laptop):
    sql_insert_into_table = """INSERT INTO lenovo_laptop VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertAsusLaptop(connection, laptop):
    sql_insert_into_table = """INSERT INTO asus_laptop VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertAcerLaptop(connection, laptop):
    sql_insert_into_table = """INSERT INTO acer_laptop VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertAppleLaptop(connection, laptop):
    sql_insert_into_table = """INSERT INTO apple_laptop VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertHpLaptop(connection, laptop):
    sql_insert_into_table = """INSERT INTO hp_laptop VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertDellLaptop(connection, laptop):
    sql_insert_into_table = """INSERT INTO dell_laptop VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)


mainUrl = 'https://www.foxtrot.com.ua'
helpArr = []
amount = []
laptopBrands = []
laptopBrandsAndAmount = {}

lenovoNamesAndUrl = []
lenovoLaptops = {}
lenovoLaptopPrices = []

asusNamesAndUrl = []
asusLaptops = {}
asusLaptopPrices = []

acerNamesAndUrl = []
acerLaptops = {}
acerLaptopPrices = []

macbookNamesAndUrl = []
macbooks = {}
macbookPrices = []

hpNamesAndUrl = []
hpLaptops = {}
hpLaptopPrices = []

dellNamesAndUrl = []
dellLaptops = {}
dellLaptopPrices = []

# БРЕНДЫ НОУТБУКОВ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('label', class_ = 'brand')
for item in helpArr:
    if item.text.strip() == 'LENOVO':
        laptopBrands.append(item.text.strip())
    elif item.text.strip() == 'ASUS': 
        laptopBrands.append(item.text.strip())
    elif item.text.strip() == 'ACER':
        laptopBrands.append(item.text.strip())
    elif item.text.strip() == 'APPLE':
        laptopBrands.append(item.text.strip())
    elif item.text.strip() == 'HP':
        laptopBrands.append(item.text.strip())
    elif item.text.strip() == 'DELL':
        laptopBrands.append(item.text.strip())
helpArr = []
helpArr = soup.find_all('span', class_ = 'amount')
for item in helpArr:
    if item.text.strip().isdigit():
        if len(amount) == 6:
            break
        amount.append(int(item.text))
helpArr = []
for i in range(0, len(laptopBrands)):
    laptopBrandsAndAmount[laptopBrands[i]] = amount[i]
#--------------------------------------------------------------------------------------


# НОУТБУКИ ЛЕНОВО
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_lenovo.html')
soup = bs(response.text, 'lxml')
lenovoNamesAndUrl = soup.find_all('a', class_ = 'card__title')
lenovoLaptopPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    lenovoLaptops[lenovoNamesAndUrl[i].text.strip()] = [int(lenovoLaptopPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + lenovoNamesAndUrl[i].get('href'))]
#----------------------------------------------------------------------------------

# НОУТБУКИ АСУС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_asus.html')
soup = bs(response.text, 'lxml')
asusNamesAndUrl = soup.find_all('a', class_ = 'card__title')
asusLaptopPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    asusLaptops[asusNamesAndUrl[i].text.strip()] = [int(asusLaptopPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + asusNamesAndUrl[i].get('href'))]
#-----------------------------------------------------------------------------------

# НОУТБУКИ ЭЙСЕР
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_acer.html')
soup = bs(response.text, 'lxml')
acerNamesAndUrl = soup.find_all('a', class_ = 'card__title')
acerLaptopPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    acerLaptops[acerNamesAndUrl[i].text.strip()] = [int(acerLaptopPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + acerNamesAndUrl[i].get('href'))]
#-----------------------------------------------------------------------------------

# МАКБУКИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_apple.html')
soup = bs(response.text, 'lxml')
macbookNamesAndUrl = soup.find_all('a', class_ = 'card__title')
macbookPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 21):
    macbooks[macbookNamesAndUrl[i].text.strip()] = [int(macbookPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + macbookNamesAndUrl[i].get('href'))]
#-----------------------------------------------------------------------------------

# НОУТБУКИ АШПИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_hp.html')
soup = bs(response.text, 'lxml')
hpNamesAndUrl = soup.find_all('a', class_ = 'card__title')
hpLaptopPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    hpLaptops[hpNamesAndUrl[i].text.strip()] = [int(hpLaptopPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + hpNamesAndUrl[i].get('href'))]
#-----------------------------------------------------------------------------------

# НОУТБУКИ ДЕЛЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_dell.html')
soup = bs(response.text, 'lxml')
dellNamesAndUrl = soup.find_all('a', class_ = 'card__title')
dellLaptopPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    dellLaptops[dellNamesAndUrl[i].text.strip()] = [int(dellLaptopPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + dellNamesAndUrl[i].get('href'))]
#---------------------------------------------------------------------