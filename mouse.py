import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs

def createTableMouseBrands(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS mouse_brands(
                            id int PRIMARY KEY NOT NULL,
                            brand_name text UNIQUE NOT NULL,
                            amount int NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertMouseBrands(connection, brand):
    sql_insert_into_table = """INSERT INTO mouse_brands VALUES(?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, brand)
        connection.commit()
    except Error as error:
        print(error)

def createLogitechMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS logitech_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertLogitechMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO logitech_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createRazerMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS razer_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertRazerMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO razer_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createAfourMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS afour_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertAfourMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO afour_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createHyperxMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS hyperx_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertHyperxMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO hyperx_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createSteelSeriesMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS steelseries_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertSteelSeriesMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO steelseries_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createAppleMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS apple_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertAppleMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO apple_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createGeniusMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS genius_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertGeniusMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO genius_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

def createLenovoMouse(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS lenovo_mouse(
                            id int PRIMARY KEY NOT NULL,
                            mouse_model text UNIQUE NOT NULL,
                            price int NOT NULL,
                            link text UNIQUE NOT NULL);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def insertLenovoMouse(connection, mouse):
    sql_insert_into_table = """INSERT INTO lenovo_mouse VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, mouse)
        connection.commit()
    except Error as error:
        print(error)

mainUrl = 'https://www.foxtrot.com.ua'
mouseBrands = []
amount = []
mouseBrandsAndAmount = {}

logitechNamesAndUrls = []
logitechPrice = []
logitech = {}

razerNameAndUrls = []
razerPrice = []
razer = {}

a4NamesAndUrls = []
a4Price = []
a4 = {}

hyperxNamesAndUrls = []
hyperxPrice = []
hyperx = {}

steelNamesAndUrls = []
steelPrice = []
steel = {}

appleNamesAndUrls = []
applePrice = []
appleMouses = {}

genuisNamesAndUrls = []
geniusPrice = []
genius = {}

lenovoNamesAndUrls = []
lenovoPrice = []
lenovoMouses = {}

response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_logitech.html')
soup = bs(response.text, 'lxml')
mouseBrands = soup.find_all('label', class_ = 'brand')
amount = soup.find_all('span', class_ = 'amount')
for i in range(0, len(mouseBrands)):
    if (mouseBrands[i].text.strip() == 'LOGITECH' or mouseBrands[i].text.strip() == 'RAZER' or mouseBrands[i].text.strip() == 'A4TECH' \
        or mouseBrands[i].text.strip() == 'HYPERX' or mouseBrands[i].text.strip() == 'STEELSERIES' or mouseBrands[i].text.strip() == 'APPLE' \
        or mouseBrands[i].text.strip() == 'GENIUS' or mouseBrands[i].text.strip() == 'LENOVO') and (int(amount[i].text.strip()) == 73\
        or int(amount[i].text.strip()) == 26 or int(amount[i].text.strip()) == 136 or int(amount[i].text.strip()) == 6\
        or int(amount[i].text.strip()) == 9 or int(amount[i].text.strip()) == 2 or int(amount[i].text.strip()) == 56 or int(amount[i].text.strip()) == 3):
        mouseBrandsAndAmount[mouseBrands[i].text.strip()] = int(amount[i].text.strip())

# МЫШИ ЛОГИТЕК
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_logitech.html')
soup = bs(response.text, 'lxml')
logitechNamesAndUrls = soup.find_all('a', class_ = 'card__title')
logitechPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    logitech[logitechNamesAndUrls[i].text.strip()] = [int(logitechPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + logitechNamesAndUrls[i].get('href'))]
#-------------------------------------------------------------------------

# МЫШИ РАЗОР
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_razer.html')
soup = bs(response.text, 'lxml')
razerNameAndUrls = soup.find_all('a', class_ = 'card__title')
razerPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    razer[razerNameAndUrls[i].text.strip()] = [int(razerPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + razerNameAndUrls[i].get('href'))]
#---------------------------------------------------------------------------------------------------------------------------

# МЫШИ А4
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_a4tech.html')
soup = bs(response.text, 'lxml')
a4NamesAndUrls = soup.find_all('a', class_ = 'card__title')
a4Price = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    a4[a4NamesAndUrls[i].text.strip()] = [int(a4Price[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + a4NamesAndUrls[i].get('href'))]
#-------------------------------------------------------------------------------------------------------------------------

# МЫШИ ГИПЕРИКС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_hyperx.html')
soup = bs(response.text, 'lxml')
hyperxNamesAndUrls = soup.find_all('a', class_ = 'card__title')
hyperxPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 6):
    hyperx[hyperxNamesAndUrls[i].text.strip()] = [int(hyperxPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + hyperxNamesAndUrls[i].get('href'))]
#--------------------------------------------------------------------------------------------------------------------------

# МЫЩИ СТИЛСИРИЭС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_steelseries.html')
soup = bs(response.text, 'lxml')
steelNamesAndUrls = soup.find_all('a', class_ = 'card__title')
steelPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 9):
    steel[steelNamesAndUrls[i].text.strip()] = [int(steelPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + steelNamesAndUrls[i].get('href'))]
#---------------------------------------------------------------------------------------------------------------------------

# МЫШИ ЭПЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_apple.html')
soup = bs(response.text, 'lxml')
appleNamesAndUrls = soup.find_all('a', class_ = 'card__title')
applePrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 2):
    appleMouses[appleNamesAndUrls[i].text.strip()] = [int(applePrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + appleNamesAndUrls[i].get('href'))]
#----------------------------------------------------------------------------------------------------------------------------

# МЫШИ ГЕНИУС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_genius.html')
soup = bs(response.text, 'lxml')
genuisNamesAndUrls = soup.find_all('a', class_ = 'card__title')
geniusPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 26):
    genius[genuisNamesAndUrls[i].text.strip()] = [int(geniusPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + genuisNamesAndUrls[i].get('href'))]
#-----------------------------------------------------------------------------------------------------------------------------

# МЫШИ ЛЕНОВО
response = requests.get('https://www.foxtrot.com.ua/ru/shop/kompyuternue_myshy_lenovo.html')
soup = bs(response.text, 'lxml')
lenovoNamesAndUrls = soup.find_all('a', class_ = 'card__title')
lenovoPrice = soup.find_all('div', class_ = 'card-price')
for i in range(0, 5):
    lenovoMouses[lenovoNamesAndUrls[i].text.strip()] = [int(lenovoPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + lenovoNamesAndUrls[i].get('href'))]