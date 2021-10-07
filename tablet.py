#26
from sqlite3.dbapi2 import Cursor
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

def createTabletBrands(conenction):
    sql_create_table = """CREATE TABLE IF NOT EXISTS tablet_brands(
                            id int PRIMARY KEY NOT NULL,
                            brand_name text UNIQUE NOT NULL,
                            amount int NOT NULL,
                            product_id int NOT NULL,
                            FOREIGN KEY (product_id) REFERENCES products (id));"""
    try:
        cursor = conenction.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createSamsungTablet(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS samsung_tablet(
                            id int PRIMARY KEY NOT NULL,
                            tablet_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tablet_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createLenovoTablet(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS lenovo_tablet(
                            id int PRIMARY KEY NOT NULL,
                            tablet_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tablet_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAppleTablet(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS apple_tablet(
                            id int PRIMARY KEY NOT NULL,
                            tablet_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tablet_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createHuaweiTablet(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS huawei_tablet(
                            id int PRIMARY KEY NOT NULL,
                            tablet_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tablet_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)
    
def createAlcatelTablet(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS alcatel_tablet(
                            id int PRIMARY KEY NOT NULL,
                            tablet_model text UNIQE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tablet_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertTabletBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO tablet_brands VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)

def insertSamsungTablet(connection, laptop):
    sql_insert_into_table = """INSERT INTO samsung_tablet VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertLenovoTablet(connection, laptop):
    sql_insert_into_table = """INSERT INTO lenovo_tablet VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertAppleTablet(connection, laptop):
    sql_insert_into_table = """INSERT INTO apple_tablet VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertHuaweiTablet(connection, laptop):
    sql_insert_into_table = """INSERT INTO huawei_tablet VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

def insertAlcatelTablet(connection, laptop):
    sql_insert_into_table = """INSERT INTO alcatel_tablet VALUES(?, ?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, laptop)
        connection.commit()
    except Error as error:
        print(error)

mainUrl = 'https://www.foxtrot.com.ua'
helpArr = []
amount = []
tabletBrands = []
tabletBrandsAndStuff = {}

samsungNamesAndUrl = []
samsungTablets = {}
samsungTabletPrices = []

lenovoNamesAndUrl = []
lenovoTablets = {}
lenovoTabletPrices = []

ipadNamesAndUrl = []
ipads = {}
ipadPrices = []

huaweiNamesAndUrl = []
huaweiTablets = {}
huaweiTabletsPrices = []

alcatelNamesAndUrl = []
alcatelTablets = {}
alcatelPrices = []

# БРЕНДЫ ПЛАНШЕТОВ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('label', class_ = 'brand')
for item in helpArr:
    if item.text.strip() == 'SAMSUNG' or item.text.strip() == 'LENOVO' or item.text.strip() == 'APPLE' or item.text.strip() == 'HUAWEI' or item.text.strip() == 'ALCATEL':
        tabletBrands.append(item.text.strip())
helpArr = []
helpArr = soup.find_all('span', class_ = 'amount')
for item in helpArr:
    if item.text.strip().isdigit():
        if len(amount) == 6:
            break
        amount.append(int(item.text))
helpArr = []
for i in range(0, len(tabletBrands)):
    tabletBrandsAndStuff[tabletBrands[i]] = amount[i]
#---------------------------------------------------------------------------------------

# ПЛАНШЕТЫ САМСУНГ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_samsung.html')
soup = bs(response.text, 'lxml')
samsungNamesAndUrl = soup.find_all('a', class_ = 'card__title')
samsungTabletPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 25):
    samsungTablets[samsungNamesAndUrl[i].text.strip()] = [int(samsungTabletPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + samsungNamesAndUrl[i].get('href'))]
#------------------------------------------------------------------------------------

# ПЛАНШЕТЫ ЛЕНОВО
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_lenovo.html')
soup = bs(response.text, 'lxml')
lenovoNamesAndUrl = soup.find_all('a', class_ = 'card__title')
lenovoTabletPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    lenovoTablets[lenovoNamesAndUrl[i].text.strip()] = [int(lenovoTabletPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + lenovoNamesAndUrl[i].get('href'))]
#-----------------------------------------------------------------------------------

# ПЛАНШЕТЫ ЭПЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_apple.html')
soup = bs(response.text, 'lxml')
ipadNamesAndUrl = soup.find_all('a', class_ = 'card__title')
ipadPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    ipads[ipadNamesAndUrl[i].text.strip()] = [int(ipadPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + ipadNamesAndUrl[i].get('href'))]
#---------------------------------------------------------------------------------

# ПЛАНШЕТЫ ХУАВЕЙ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_huawei.html')
soup = bs(response.text, 'lxml')
huaweiNamesAndUrl = soup.find_all('a', class_ = 'card__title')
huaweiTabletsPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 11):
    huaweiTablets[huaweiNamesAndUrl[i].text.strip()] = [int(huaweiTabletsPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + huaweiNamesAndUrl[i].get('href'))]
#----------------------------------------------------------------------------------------

# ПЛАНШЕТЫ АЛКАТЕЛЬ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_alcatel.html')
soup = bs(response.text, 'lxml')
alcatelNamesAndUrl = soup.find_all('a', class_ = 'card__title')
alcatelPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 9):
    alcatelTablets[alcatelNamesAndUrl[i].text.strip()] = [int(alcatelPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + alcatelNamesAndUrl[i].get('href'))]
#-------------------------------------------------------------------------------------
