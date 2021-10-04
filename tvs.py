#5
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

samsungNames = []
urlsSamsung = []
samsungTvs = {}
samsungPrices = []

lgNames = []
urlsLg = []
lgTvs = {}
lgPrices = []

xiaomiNames = []
urlsXiaomi = []
xiaomiTvs = {}
xiaomiPrices = []

sonyNames = []
urlsSony = []
sonyTvs = {}
sonyPrices = []

philipsNames = []
urlsPhilips = []
philipsTvs = {}
philipsPrices = []

toshibaNames = []
urlsToshiba = []
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
        if item.text.strip() == '99':
            amount.append(int(item.text))
        elif item.text.strip() == '68':
            amount.append(int(item.text))
        elif item.text.strip() == '3':
            amount.append(int(item.text))
        elif item.text.strip() == '43':
            amount.append(int(item.text))
        elif item.text.strip() == '31':
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
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    samsungNames.append(item.text.strip())
    urlsSamsung.append(item.get('href'))
helpArr = []
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('div', class_ = 'card-price')
samsungPrices = returnPrice(helpArr)
helpArr = []
for samsungName in samsungNames:
    samsungTvs[samsungName] = []
    for i in range(0, len(samsungPrices)):
        samsungTvs[samsungName].append(samsungPrices[i])
        samsungPrices.remove(samsungPrices[i])
        for j in range(0, len(urlsSamsung)):
            samsungTvs[samsungName].append(str(mainUrl + urlsSamsung[j]))
            urlsSamsung.remove(urlsSamsung[j])
            break
        break
#---------------------------------------------------------------------------------------

# TV LG
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_lg.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    lgNames.append(item.text.strip())
    urlsLg.append(item.get('href'))
helpArr = []
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('div', class_ = 'card-price')
lgPrices = returnPrice(helpArr)
helpArr = []
for lgName in lgNames:
    lgTvs[lgName] = []
    for i in range(0, len(lgPrices)):
        lgTvs[lgName].append(lgPrices[i])
        lgPrices.remove(lgPrices[i])
        for j in range(0, len(urlsLg)):
            lgTvs[lgName].append(str(mainUrl + urlsLg[j]))
            urlsLg.remove(urlsLg[j])
            break
        break
#----------------------------------------------------------------------------------------

# TV XIAOMI
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_xiaomi.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(xiaomiNames) == 3 and len(urlsXiaomi) == 3:
        break
    xiaomiNames.append(item.text.strip())
    urlsXiaomi.append(item.get('href'))
helpArr = []
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('div', class_ = 'card-price')
xiaomiPrices = returnPrice(helpArr)
helpArr = []
for xiaomiName in xiaomiNames:
    xiaomiTvs[xiaomiName] = []
    for i in range(0, len(xiaomiPrices)):
        xiaomiTvs[xiaomiName].append(xiaomiPrices[i])
        xiaomiPrices.remove(xiaomiPrices[i])
        for j in range(0, len(urlsXiaomi)):
            xiaomiTvs[xiaomiName].append(str(mainUrl + urlsXiaomi[j]))
            urlsXiaomi.remove(urlsXiaomi[j])
            break
        break
#--------------------------------------------------------------------------------------

# TV SONY
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_sony.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    sonyNames.append(item.text.strip())
    urlsSony.append(item.get('href'))
helpArr = []
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('div', class_ = 'card-price')
sonyPrices = returnPrice(helpArr)
helpArr = []
for sonyName in sonyNames:
    sonyTvs[sonyName] = []
    for i in range(0, len(sonyPrices)):
        sonyTvs[sonyName].append(sonyPrices[i])
        sonyPrices.remove(sonyPrices[i])
        for j in range(0, len(urlsSony)):
            sonyTvs[sonyName].append(str(mainUrl + urlsSony[j]))
            urlsSony.remove(urlsSony[j])
            break
        break
#------------------------------------------------------------------------------------

# TV PHILIPS
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_philips.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    philipsNames.append(item.text.strip())
    urlsPhilips.append(item.get('href'))
helpArr = []
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('div', class_ = 'card-price')
philipsPrices = returnPrice(helpArr)
helpArr = []
for philipsName in philipsNames:
    philipsTvs[philipsName] = []
    for i in range(0, len(philipsPrices)):
        philipsTvs[philipsName].append(philipsPrices[i])
        philipsPrices.remove(philipsPrices[i])
        for j in range(0, len(urlsPhilips)):
            philipsTvs[philipsName].append(str(mainUrl + urlsPhilips[j]))
            urlsPhilips.remove(urlsPhilips[j])
            break
        break
#-----------------------------------------------------------------------------------------

#TV TOSHIBA
response = requests.get('https://www.foxtrot.com.ua/ru/shop/led_televizory_philips.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(toshibaNames) == 11 and len(urlsToshiba) == 11:
        break
    toshibaNames.append(item.text.strip())
    urlsToshiba.append(item.get('href'))
helpArr = []
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('div', class_ = 'card-price')
toshibaPrices = returnPrice(helpArr)
helpArr = []
for toshibaName in toshibaNames:
    toshibaTvs[toshibaName] = []
    for i in range(0, len(toshibaPrices)):
        toshibaTvs[toshibaName].append(toshibaPrices[i])
        toshibaPrices.remove(toshibaPrices[i])
        for j in range(0, len(urlsToshiba)):
            toshibaTvs[toshibaName].append(str(mainUrl + urlsToshiba[j]))
            urlsToshiba.remove(urlsToshiba[j])
            break
        break
#---------------------------------------------------------------------------------------