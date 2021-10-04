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

lenovoNames = []
urlsLenovo = []
lenovoLaptops = {}
lenovoLaptopPrices = []

asusNames = []
urlsAsus = []
asusLaptops = {}
asusLaptopPrices = []

acerNames = []
urlsAcer = []
acerLaptops = {}
acerLaptopPrices = []

macbookNames = []
urlsMacbooks = []
macbooks = {}
macbookPrices = []

hpNames = []
urlsHp = []
hpLaptops = {}
hpLaptopPrices = []

dellNames = []
urlsDell = []
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
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    lenovoNames.append(item.text.strip())
    urlsLenovo.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
lenovoLaptopPrices = returnPrice(helpArr)
helpArr = []
for lenovoName in lenovoNames:

    lenovoLaptops[lenovoName] = []
    for i in range(0, len(lenovoLaptopPrices)):
        lenovoLaptops[lenovoName].append(lenovoLaptopPrices[i])
        lenovoLaptopPrices.remove(lenovoLaptopPrices[i])
        for j in range(0, len(urlsLenovo)):
            lenovoLaptops[lenovoName].append(str(mainUrl + urlsLenovo[j]))
            urlsLenovo.remove(urlsLenovo[j])
            break
        break
#----------------------------------------------------------------------------------

# НОУТБУКИ АСУС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_asus.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    asusNames.append(item.text.strip())
    urlsAsus.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
asusLaptopPrices = returnPrice(helpArr)
helpArr = []
for asusName in asusNames:
    asusLaptops[asusName] = []
    for i in range(0, len(asusLaptopPrices)):
        asusLaptops[asusName].append(asusLaptopPrices[i])
        asusLaptopPrices.remove(asusLaptopPrices[i])
        for j in range(0, len(urlsAsus)):
            asusLaptops[asusName].append(str(mainUrl + urlsAsus[j]))
            urlsAsus.remove(urlsAsus[j])
            break
        break
#-----------------------------------------------------------------------------------


# НОУТБУКИ ЭЙСЕР
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_acer.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    acerNames.append(item.text.strip())
    urlsAcer.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
acerLaptopPrices = returnPrice(helpArr)
helpArr = []
for acerName in acerNames:
    acerLaptops[acerName] = []
    for i in range(0, len(acerLaptopPrices)):
        acerLaptops[acerName].append(acerLaptopPrices[i])
        acerLaptopPrices.remove(acerLaptopPrices[i])
        for j in range(0, len(urlsAcer)):
            acerLaptops[acerName].append(str(mainUrl + urlsAcer[j]))
            urlsAcer.remove(urlsAcer[j])
            break
        break
#-----------------------------------------------------------------------------------

# МАКБУКИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_apple.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(macbookNames) == 21 and len(urlsMacbooks) == 21:
        break
    macbookNames.append(item.text.strip())
    urlsMacbooks.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
macbookPrices = returnPrice(helpArr)
helpArr = []
for macbookName in macbookNames:
    macbooks[macbookName] = []
    for i in range(0, len(macbookPrices)):
        macbooks[macbookName].append(macbookPrices[i])
        macbookPrices.remove(macbookPrices[i])
        for j in range(0, len(urlsMacbooks)):
            macbooks[macbookName].append(urlsMacbooks[j])
            urlsMacbooks.remove(str(mainUrl + urlsMacbooks[j]))
            break
        break
#-----------------------------------------------------------------------------------

# НОУТБУКИ АШПИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_hp.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    hpNames.append(item.text.strip())
    urlsHp.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
hpLaptopPrices = returnPrice(helpArr)
helpArr = []
for hpName in hpNames:
    hpLaptops[hpName] = []
    for i in range(0, len(hpLaptopPrices)):
        hpLaptops[hpName].append(hpLaptopPrices[i])
        hpLaptopPrices.remove(hpLaptopPrices[i])
        for j in range(0, len(urlsHp)):
            hpLaptops[hpName].append(str(mainUrl + urlsHp[j]))
            urlsHp.remove(urlsHp[j])
            break
        break
#-----------------------------------------------------------------------------------

# НОУТБУКИ ДЕЛЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/noutbuki_dell.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    dellNames.append(item.text.strip())
    urlsDell.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
dellLaptopPrices = returnPrice(helpArr)
helpArr = []
for dellName in dellNames:
    dellLaptops[dellName] = []
    for i in range(0, len(dellLaptopPrices)):
        dellLaptops[dellName].append(dellLaptopPrices[i])
        for j in range(0, len(urlsDell)):
            dellLaptops[dellName].append(urlsDell[j])
            urlsDell.remove(str(mainUrl + urlsDell[j]))
            break
        break
#------------------------------------------------------------------------------------