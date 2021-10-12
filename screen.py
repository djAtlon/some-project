import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs


def getPrice(helpArr):
    priceArr = []
    for item in helpArr:
        price = item.text.strip()
        new_price = price.split('₴')[0]
        firstPart = new_price.split(' ')[0]
        secondPart = new_price.split(' ')[1]
        priceArr.append(int(firstPart + secondPart))
    return priceArr

def createTableScreenBrands(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS screen_brands(
                            id int PRIMARY KEY NOT NULL,
                            brand_name text UNIQUE NOT NULL,
                            amount int NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createSamsungScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS samsung_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createMsiScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS msi_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAsusScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS asus_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createLgScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS lg_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createDellScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS dell_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createBenqScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS benq_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAocScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS aoc_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createGigabyteScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS gigabyte_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createAcerScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS acer_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createHpScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS hp_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createPhilipsScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS philips_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createLenovoScreen(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS lenovo_screen(
                            id int PRIMARY KEY NOT NULL,
                            screen_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertSamsungScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO samsung_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertMsiScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO msi_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertAsusScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO asus_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertLgScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO lg_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertDellScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO dell_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertBenqScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO benq_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertAocScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO aoc_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertGigabytecreen(connection, screen):
    sql_insert_into_table = """INSERT INTO gigabyte_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertAcerScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO acer_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertHpScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO hp_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertPhilipsScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO philips_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertLenovoScreen(connection, screen):
    sql_insert_into_table = """INSERT INTO lenovo_screen VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, screen)
        connection.commit()
    except Error as error:
        print(error)

def insertScreenBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO screen_brands VALUES(?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)

mainUrl = 'https://www.foxtrot.com.ua'
helpArr = []

screenBrands = []
amount = []
screenBrandsAndAmount = {}

samsungNamesAndUrls = []
samsungScreens = {}
samsungPrices = []

msiNamesAndUrls = []
msiScreens = {}
msiPrices = []

asusNamesAndUrls = []
asusScreens = {}
asusPrices = []

lgNamesAndUrls = []
lgScreens = {}
lgPrices = []

dellNamesAndUrls = []
dellScreens = {}
dellPrices = []

benqNamesAndUrls = []
benqScreens = {}
benqPrices = []

aocNamesAndUrls = []
aocPrices = []
aocScreens = {}


gigabyteNamesAndUrls = []
gigabyteScreens = {}
gigabytePrices = []

acerNamesAndUrls = []
acerScreens = {}
acerPrices = []

hpNamesAndUrls = []
hpScreens = {}
hpPrices = []

philipsNamesAndUrls = []
philipsScreens = {}
philipsPrices = []

lenovoNamesAndUrls = []
lenovoScreens = {}
lenovoPrices = []

response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('label', class_ = 'brand')
for item in helpArr:
    if item.text.strip() == 'Кредит 0,01%' or item.text.strip() == 'Оплата частями' or item.text.strip() == 'Акции' or item.text.strip() == 'Скидки':
        continue
    if len(screenBrands) == 12:
        break
    screenBrands.append(item.text.strip())
helpArr = []
helpArr = soup.find_all('span', class_ = 'amount')
for item in helpArr:
    if len(amount) == 12:
        break
    if item.text.strip().isdigit():
        amount.append(int(item.text))
helpArr = []
for i in range(0, len(screenBrands)):
    screenBrandsAndAmount[screenBrands[i]] = amount[i]

# МОНИТОРЫ САМСУНГ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_samsung.html')
soup = bs(response.text, 'lxml')
samsungNamesAndUrls = soup.find_all('a', class_= 'card__title')
samsungPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    samsungScreens[samsungNamesAndUrls[i].text.strip()] = [int(samsungPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + samsungNamesAndUrls[i].get('href'))]
#-------------------------------------------------------------------------------

# МОНИТОРЫ МСИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_msi.html')
soup = bs(response.text, 'lxml')
msiNamesAndUrls = soup.find_all('a', class_= 'card__title')
msiPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    msiScreens[msiNamesAndUrls[i].text.strip()] = [int(msiPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + msiNamesAndUrls[i].get('href'))]
#-------------------------------------------------------------------------------

# МОНИТОРЫ АСУС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_asus.html')
soup = bs(response.text, 'lxml')
asusNamesAndUrls = soup.find_all('a', class_= 'card__title')
asusPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    asusScreens[asusNamesAndUrls[i].text.strip()] = [int(asusPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + asusNamesAndUrls[i].get('href'))]
#-------------------------------------------------------------------------------

# МОНИТОРЫ ЛГ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_lg.html')
soup = bs(response.text, 'lxml')
lgNamesAndUrls = soup.find_all('a', class_= 'card__title')
lgPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    lgScreens[lgNamesAndUrls[i].text.strip()] = [int(lgPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + lgNamesAndUrls[i].get('href'))]
#--------------------------------------------------------------------------------

# МОНИТОРЫ ДЕЛЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_dell.html')
soup = bs(response.text, 'lxml')
dellNamesAndUrls = soup.find_all('a', class_= 'card__title')
dellPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 22):
    dellScreens[dellNamesAndUrls[i].text.strip()] = [int(dellPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + dellNamesAndUrls[i].get('href'))]
#------------------------------------------------------------------------------

# МОНИТОРЫ БЕНКЬЮ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_benq.html')
soup = bs(response.text, 'lxml')
benqNamesAndUrls = soup.find_all('a', class_= 'card__title')
benqPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    benqScreens[benqNamesAndUrls[i].text.strip()] = [int(benqPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + benqNamesAndUrls[i].get('href'))]
#------------------------------------------------------------------------------

# МОНИТОРЫ АОК
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_aoc.html')
soup = bs(response.text, 'lxml')
aocNamesAndUrls = soup.find_all('a', class_= 'card__title')
aocPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    aocScreens[aocNamesAndUrls[i].text.strip()] = [int(aocPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + aocNamesAndUrls[i].get('href'))]
#-------------------------------------------------------------------------------

# МОНИТОРЫ ГИГАБАЙТ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_gigabyte.html')
soup = bs(response.text, 'lxml')
gigabyteNamesAndUrls = soup.find_all('a', class_= 'card__title')
gigabytePrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 15):
    gigabyteScreens[gigabyteNamesAndUrls[i].text.strip()] = [int(gigabytePrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + gigabyteNamesAndUrls[i].get('href'))]
#----------------------------------------------------------------------------------

# МОНИТОРЫ АСЕР
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_acer.html')
soup = bs(response.text, 'lxml')
acerNamesAndUrls = soup.find_all('a', class_= 'card__title')
acerPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    acerScreens[acerNamesAndUrls[i].text.strip()] = [int(acerPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + acerNamesAndUrls[i].get('href'))]

# --------------------------------------------------------------------------------

# МОНИТОРЫ АШПИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_hp.html')
soup = bs(response.text, 'lxml')
hpNamesAndUrls = soup.find_all('a', class_= 'card__title')
hpPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    hpScreens[hpNamesAndUrls[i].text.strip()] = [int(hpPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + hpNamesAndUrls[i].get('href'))]
# ----------------------------------------------------------------------------------

# МОНИТОРЫ ФИЛИПС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_philips.html')
soup = bs(response.text, 'lxml')
philipsNamesAndUrls = soup.find_all('a', class_= 'card__title')
philipsPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    philipsScreens[philipsNamesAndUrls[i].text.strip()] = [int(philipsPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + philipsNamesAndUrls[i].get('href'))]
#----------------------------------------------------------------------------------------

# МОНИТОРЫ ЛЕНОВО
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_lenovo.html')
soup = bs(response.text, 'lxml')
lenovoNamesAndUrls = soup.find_all('a', class_= 'card__title')
lenovoPrices = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    lenovoScreens[lenovoNamesAndUrls[i].text.strip()] = [int(lenovoPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + lenovoNamesAndUrls[i].get('href'))]
#---------------------------------------------------------------------------------------