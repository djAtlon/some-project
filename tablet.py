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
                            FOREIGN (product_id) KEY REFERENCES products (id));"""
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

def insertTabletpBrands(connection, brand):
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

samsungNames = []
urlsSamsung = []
samsungTablets = {}
samsungTabletPrices = []

lenovoNames = []
urlsLenovo = []
lenovoTablets = {}
lenovoTabletPrices = []

ipadNames = []
urlsIpad = []
ipads = {}
ipadPrices = []

huaweiNames = []
urlsHuawei = []
huaweiTablets = {}
huaweiTabletsPrices = []

alcatelNames = []
urlsAlcatel = []
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
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(samsungNames) == 20 and len(urlsSamsung) == 20:
        break
    samsungNames.append(item.text.strip())
    urlsSamsung.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
samsungTabletPrices = returnPrice(helpArr)
count = 0
while count != 8:
    samsungTabletPrices.pop(-1)
    count += 1
helpArr = []
for sammsungName in samsungNames:
    samsungTablets[sammsungName] = []
    for i in range(0, len(samsungTabletPrices)):
        samsungTablets[sammsungName].append(samsungTabletPrices[i])
        samsungTabletPrices.remove(samsungTabletPrices[i])
        for j in range(0, len(urlsSamsung)):
            samsungTablets[sammsungName].append(str(mainUrl + urlsSamsung[j]))
            urlsSamsung.remove(urlsSamsung[j])
            break
        break
#------------------------------------------------------------------------------------

# ПЛАНШЕТЫ ЛЕНОВО
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_lenovo.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(lenovoNames) == 26 and len(urlsLenovo) == 26:
        break
    lenovoNames.append(item.text.strip())
    urlsLenovo.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
lenovoTabletPrices = returnPrice(helpArr)
count = 0
while count != 8:
    lenovoTabletPrices.pop(-1)
    count += 1
for lenovoName in lenovoNames:
    lenovoTablets[lenovoName] = []
    for i in range(0, len(lenovoTabletPrices)):
        lenovoTablets[lenovoName].append(lenovoTabletPrices[i])
        lenovoTabletPrices.remove(lenovoTabletPrices[i])
        for j in range(0, len(urlsLenovo)):
            lenovoTablets[lenovoName].append(str(mainUrl + urlsLenovo[j]))
            urlsLenovo.remove(urlsLenovo[j])
            break
        break
#-----------------------------------------------------------------------------------

# ПЛАНШЕТЫ ЭПЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_apple.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(ipadNames) == 26 and len(urlsIpad) == 26:
        break
    ipadNames.append(item.text.strip())
    urlsIpad.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
ipadPrices = returnPrice(helpArr)
count = 0
while count != 8:
    ipadPrices.pop(-1)
    count += 1
helpArr = []
for ipadName in ipadNames:
    ipads[ipadName] = []
    for i in range(0, len(ipadPrices)):
        ipads[ipadName].append(ipadPrices[i])
        ipadPrices.remove(ipadPrices[i])
        for j in range(0, len(urlsIpad)):
            ipads[ipadName].append(str(mainUrl + urlsIpad[j]))
            urlsIpad.remove(urlsIpad[j])
            break
        break
#---------------------------------------------------------------------------------

# ПЛАНШЕТЫ ХУАВЕЙ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_huawei.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(huaweiNames) == 13 and len(urlsHuawei) == 13:
        break
    huaweiNames.append(item.text.strip())
    urlsHuawei.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
huaweiTabletsPrices = returnPrice(helpArr)
count = 0
while count != 5:
    huaweiTabletsPrices.pop(-1)
    count += 1
helpArr = []
for huaweiName in huaweiNames:
    huaweiTablets[huaweiName] = []
    for i in range(0, len(huaweiTabletsPrices)):
        huaweiTablets[huaweiName].append(huaweiTabletsPrices[i])
        huaweiTabletsPrices.remove(huaweiTabletsPrices[i])
        for j in range(0, len(urlsHuawei)):
            huaweiTablets[huaweiName].append(str(mainUrl + urlsHuawei[j]))
            urlsHuawei.remove(urlsHuawei[j])
            break
        break
#----------------------------------------------------------------------------------------

# ПЛАНШЕТЫ АЛКАТЕЛЬ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/planshety_alcatel.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_ = 'card__title')
for item in helpArr:
    if len(alcatelNames) == 9 and len(urlsAlcatel) == 9:
        break
    alcatelNames.append(item.text.strip())
    urlsAlcatel.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
alcatelPrices = returnPrice(helpArr)
count = 0
while count != 4:
    alcatelPrices.pop(-1)
    count += 1
helpArr = []
for alcatelName in alcatelNames:
    alcatelTablets[alcatelName] = []
    for i in range(0, len(alcatelPrices)):
        alcatelTablets[alcatelName].append(alcatelPrices[i])
        alcatelPrices.remove(alcatelPrices[i])
        for j in range(0, len(urlsAlcatel)):
            alcatelTablets[alcatelName].append(str(mainUrl + urlsAlcatel[j]))
            urlsAlcatel.remove(urlsAlcatel[j])
            break
        break
#-------------------------------------------------------------------------------------
