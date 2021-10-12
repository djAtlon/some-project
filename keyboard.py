import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs

def createKeyboardBrands(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS keyboard_brands(
                            id int PRIMARY KEY NOT NULL,
                            brand_name text UNIQUE NOT NULL,
                            amount int NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertKeyboardBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO keyboard_brands VALUES (?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)

def createLogitechKeyboard(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS logitech_keyboard(
                            id int PRIMARY KEY NOT NULL,
                            keyboard_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertLogitechKeyboard(connection, keyboard):
    sql_insert_into_table = """INSERT INTO logitech_keyboard VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, keyboard)
        connection.commit()
    except Error as error:
        print(error)

def createHyperxKeyboard(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS hyperx_keyboard(
                            id int PRIMARY KEY NOT NULL,
                            keyboard_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertHyperxKeyboard(connection, keyboard):
    sql_insert_into_table = """INSERT INTO hyperx_keyboard VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, keyboard)
        connection.commit()
    except Error as error:
        print(error)

def createRazerKeyboard(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS razer_keyboard(
                            id int PRIMARY KEY NOT NULL,
                            keyboard_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertRazerKeyboard(connection, keyboard):
    sql_insert_into_table = """INSERT INTO razer_keyboard VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, keyboard)
        connection.commit()
    except Error as error:
        print(error)

def createMsiKeyboard(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS msi_keyboard(
                            id int PRIMARY KEY NOT NULL,
                            keyboard_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertMsiKeyboard(connection, keyboard):
    sql_insert_into_table = """INSERT INTO msi_keyboard VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, keyboard)
        connection.commit()
    except Error as error:
        print(error)

def createAfourTechKeyboard(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS afour_keyboard(
                            id int PRIMARY KEY NOT NULL,
                            keyboard_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertAfourKeyboard(connection, keyboard):
    sql_insert_into_table = """INSERT INTO afour_keyboard VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, keyboard)
        connection.commit()
    except Error as error:
        print(error)

def createAppleKeyboard(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS apple_keyboard(
                            id int PRIMARY KEY NOT NULL,
                            keyboard_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertAppleKeyboard(connection, keyboard):
    sql_insert_into_table = """INSERT INTO apple_keyboard VALUES (?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, keyboard)
        connection.commit()
    except Error as error:
        print(error)

mainUrl = 'https://www.foxtrot.com.ua'
keyboardBrands = []
amount = []
keyboardBrandsAndAmount = {}

logitechNamesAndUrls = []
logitechPrice = []
logitechKeyboards = {}

hyperxNamesAndUrls = []
hyperxPrice = []
hyperxKeyboards = {}

razerNamesAndUrls = []
razerPrice = []
razerKeyboards = {}

msiNamesAndUrls = []
msiPrice = []
msiKeyboards = {}

a4NamesAndUrls = []
a4Price = []
a4Keyboards = {}

appleNamesAndUrls = []
applePrice = []
appleKeyboards = {}

response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury.html')
soup = bs(response.text, 'lxml')
keyboardBrands = soup.find_all('label', class_ = 'brand')
amount = soup.find_all('span', class_ = 'amount')
for i in range(0, len(keyboardBrands)):
    if (keyboardBrands[i].text.strip() == 'LOGITECH' or keyboardBrands[i].text.strip() == 'HYPERX' or keyboardBrands[i].text.strip() == 'RAZER' \
        or keyboardBrands[i].text.strip() == 'MSI' or keyboardBrands[i].text.strip() == 'A4TECH' or keyboardBrands[i].text.strip() == 'APPLE') and \
            (int(amount[i].text.strip()) == 35 or int(amount[i].text.strip()) == 9 or int(amount[i].text.strip()) == 32 \
                or int(amount[i].text.strip()) == 5 or int(amount[i].text.strip()) == 67 or int(amount[i].text.strip()) == 5):
                keyboardBrandsAndAmount[keyboardBrands[i].text.strip()] = int(amount[i].text.strip())

# КЛАВИАТУРА ЛОГИТЕК
response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury_logitech.html')
soup = bs(response.text, 'lxml')
logitechNamesAndUrls = soup.find_all('a', class_ = 'card__title')
logitechPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    logitechKeyboards[logitechNamesAndUrls[i].text.strip()] = [int(logitechPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + logitechNamesAndUrls[i].get('href'))]
#---------------------------------------------------------------------------------

# КЛАВИАТУРА ГИПЕРИКС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury_hyperx.html')
soup = bs(response.text, 'lxml')
hyperxNamesAndUrls = soup.find_all('a', class_ = 'card__title')
hyperxPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 9):
    hyperxKeyboards[hyperxNamesAndUrls[i].text.strip()] = [int(hyperxPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + hyperxNamesAndUrls[i].get('href'))]
#----------------------------------------------------------------------------------

# КЛАВИАТУРА РАЗЕР
response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury_razer.html')
soup = bs(response.text, 'lxml')
razerNamesAndUrls = soup.find_all('a', class_ = 'card__title')
razerPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    razerKeyboards[razerNamesAndUrls[i].text.strip()] = [int(razerPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + razerNamesAndUrls[i].get('href'))]
#----------------------------------------------------------------------------------

# КЛАВИАТУРА МСИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury_msi.html')
soup = bs(response.text, 'lxml')
msiNamesAndUrls = soup.find_all('a', class_ = 'card__title')
msiPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 5):
    msiKeyboards[msiNamesAndUrls[i].text.strip()] = [int(msiPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + msiNamesAndUrls[i].get('href'))]
#---------------------------------------------------------------------------------

# КЛАВИАТУРА А4
response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury_a4tech.html')
soup = bs(response.text, 'lxml')
a4NamesAndUrls = soup.find_all('a', class_ = 'card__title')
a4Price = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    a4Keyboards[a4NamesAndUrls[i].text.strip()] = [int(a4Price[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + a4NamesAndUrls[i].get('href'))]
#-----------------------------------------------------------------------------------

# КЛАВИАТУРА ЭПЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/klaviatury_apple.html')
soup = bs(response.text, 'lxml')
appleNamesAndUrls = soup.find_all('a', class_ = 'card__title')
applePrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 5):
    appleKeyboards[appleNamesAndUrls[i].text.strip()] = [int(applePrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + appleNamesAndUrls[i].get('href'))]