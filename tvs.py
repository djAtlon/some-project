#5
from sqlite3.dbapi2 import SQLITE_DROP_VIEW
import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs
from requests.models import Response

def returnPrice(helpArr):
    priceArr = []
    for item in helpArr:
        price = item.text.strip()
        new_price = price.split('₴')[0]
        firstPart = new_price.split(' ')[0]
        secondPart = new_price.split(' ')[1]
        priceArr.append(int(firstPart + secondPart))
    return priceArr


def createTvBrands(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS tv_brands(
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


def createSamsungTv(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS samsung_tv(
                            id int PRIMARY KEY NOT NULL,
                            tv_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tv_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createLgTv(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS lg_tv(
                            id int PRIMARY KEY NOT NULL,
                            tv_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tv_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createXiaomiTv(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS xiaomi_tv(
                            id int PRIMARY KEY NOT NULL,
                            tv_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tv_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createSonyTv(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS sony_tv(
                            id int PRIMARY KEY NOT NULL,
                            tv_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tv_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createPhilipsTv(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS philips_tv(
                            id int PRIMARY KEY NOT NULL,
                            tv_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tv_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def createToshibaTv(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS toshiba_tv(
                            id int PRIMARY KEY NOT NULL,
                            tv_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            brand_id int NOT NULL,
                            link text UNIQUE NOT NULL,
                            FOREIGN KEY (brand_id) REFERENCES tv_brands (id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)


def insertTvBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO tv_brands VALUES(?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)


def insertSamsungTv(connection, tv):
    sql_insert_into_table = """INSERT INTO samsung_tv VALUES (?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, tv)
        connection.commit()
    except Error as error:
        print(error)

def insertLgTv(connection, tv):
    sql_insert_into_table = """INSERT INTO lg_tv VALUES (?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, tv)
        connection.commit()
    except Error as error:
        print(error)


def insertXiaomiTv(connection, tv):
    sql_insert_into_table = """INSERT INTO xiaomi_tv VALUES (?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, tv)
        connection.commit()
    except Error as error:
        print(error)


def insertSonyTv(connection, tv):
    sql_insert_into_table = """INSERT INTO sony_tv VALUES (?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, tv)
        connection.commit()
    except Error as error:
        print(error)

def insertPhilipsTv(connection, tv):
    sql_insert_into_table = """INSERT INTO philips_tv VALUES (?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, tv)
        connection.commit()
    except Error as error:
        print(error)


def insertToshibaTv(connection, tv):
    sql_insert_into_table = """INSERT INTO toshiba_tv VALUES (?,?,?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, tv)
        connection.commit()
    except Error as error:
        print(error)

mainUrl = 'https://www.foxtrot.com.ua'
helpArr = []
amount = []
tvBrands = []
tvBrandsAndStuff = {}

samsungNamesAndUrl = []
samsungTvs = {}
samsungPrices = []

lgNamesAndUrl = []
lgTvs = {}
lgPrices = []

xiaomiNamesAndUrl = []
xiaomiTvs = {}
xiaomiPrices = []

sonyNamesAndUrl = []
sonyTvs = {}
sonyPrices = []

philipsNamesAndUrl = []
philipsTvs = {}
philipsPrices = []

toshibaNamesAndUrl = []
toshibaTvs = {}
toshibaPrices = []

response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('label', class_ = 'brand')
for item in helpArr:
    if item.text.strip() == 'SAMSUNG':
        tvBrands.append(item.text.strip())
    elif item.text.strip() == 'LG':
        tvBrands.append(item.text.strip())
    elif item.text.strip() == 'XIAOMI':
        tvBrands.append(item.text.strip())
    elif item.text.strip() == 'SONY':
        tvBrands.append(item.text.strip())
    elif item.text.strip() == 'PHILIPS':
        tvBrands.append(item.text.strip())
    elif item.text.strip() == 'TOSHIBA':
        tvBrands.append(item.text.strip())
helpArr = []
helpArr = soup.find_all('span', class_ = 'amount')
for item in helpArr:
    if item.text.strip().isdigit():
        if len(amount) == 5:
            break
        if item.text.strip() == '96':
            amount.append(int(item.text))
        elif item.text.strip() == '66':
            amount.append(int(item.text))
        elif item.text.strip() == '3':
            amount.append(int(item.text))
        elif item.text.strip() == '43':
            amount.append(int(item.text))
        elif item.text.strip() == '30':
            amount.append(int(item.text))

amount.append(11)
# amount.pop(len(amount)-2)
# amount.pop(len(amount)-2)
for i in range(0, len(tvBrands)):
    tvBrandsAndStuff[tvBrands[i]] = amount[i]
helpArr = []

# TV SAMSUNG
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_samsung.html')
soup = bs(response.text, 'lxml')
samsungNamesAndUrl = soup.find_all('a', class_ = 'card__title')
samsungPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    samsungTvs[samsungNamesAndUrl[i].text.strip()] = [samsungPrices[i].text.strip().replace(' ', '').split('₴')[0], str(mainUrl + samsungNamesAndUrl[i].get('href'))]
#---------------------------------------------------------------------------------------

# TV LG
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_lg.html')
soup = bs(response.text, 'lxml')
lgNamesAndUrl = soup.find_all('a', class_ = 'card__title')
lgPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    lgTvs[lgNamesAndUrl[i].text.strip()] = [int(lgPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + lgNamesAndUrl[i].get('href'))]
#----------------------------------------------------------------------------------------

# TV XIAOMI
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_xiaomi.html')
soup = bs(response.text, 'lxml')
xiaomiNamesAndUrl = soup.find_all('a', class_ = 'card__title')
xiaomiPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 3):
    xiaomiTvs[xiaomiNamesAndUrl[i].text.strip()] = [int(xiaomiPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + xiaomiNamesAndUrl[i].get('href'))]
#--------------------------------------------------------------------------------------

# TV SONY
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_sony.html')
soup = bs(response.text, 'lxml')
sonyNamesAndUrl = soup.find_all('a', class_ = 'card__title')
sonyPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    sonyTvs[sonyNamesAndUrl[i].text.strip()] = [int(sonyPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + sonyNamesAndUrl[i].get('href'))]
#------------------------------------------------------------------------------------

# TV PHILIPS
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_philips.html')
soup = bs(response.text, 'lxml')
philipsNamesAndUrl = soup.find_all('a', class_ = 'card__title')
philipsPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    philipsTvs[philipsNamesAndUrl[i].text.strip()] = [int(philipsPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + philipsNamesAndUrl[i].get('href'))]
#-----------------------------------------------------------------------------------------

#TV TOSHIBA
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_philips.html')
soup = bs(response.text, 'lxml')
toshibaNamesAndUrl = soup.find_all('a', class_ = 'card__title')
toshibaPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 11):
    toshibaTvs[toshibaNamesAndUrl[i].text.strip()] = [int(toshibaPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + toshibaNamesAndUrl[i].get('href'))]
#---------------------------------------------------------------------------------------