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

samsungNames = []
urlsSamsung = []
samsungScreens = {}
samsungPrices = []

msiNames = []
urlsMsi = []
msiScreens = {}
msiPrices = []

asusNames = []
urlsAsus = []
asusScreens = {}
asusPrices = []

lgNames = []
urlsLg = []
lgScreens = {}
lgPrices = []

dellNames = []
urlsDell = []
dellScreens = {}
dellPrices = []

benqNames = []
urlsBenq = []
benqScreens = {}
benqPrices = []

aocNames = []
urlsAoc = []
aocScreens = {}
aocPrices = []

gigabyteNames = []
urlsGigabyte = []
gigabyteScreens = {}
gigabytePrices = []

acerNames = []
urlsAcer = []
acerScreens = {}
acerPrices = []

hpNames = []
urlsHp = []
hpScreens = {}
hpPrices = []

philipsNames = []
urlsPhilips = []
philipsScreens = {}
philipsPrices = []

lenovoNames = []
urlsLenovo = []
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
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(samsungNames) == 26 and len(urlsSamsung) == 26:
        break
    samsungNames.append(item.text.strip())
    urlsSamsung.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
samsungPrices = getPrice(helpArr)
count = 0
while count != 8:
    samsungPrices.pop(-1)
    count += 1
helpArr = []
for samsungName in samsungNames:
    samsungScreens[samsungName] = []
    for i in range(0, len(samsungPrices)):
        samsungScreens[samsungName].append(samsungPrices[i])
        samsungPrices.remove(samsungPrices[i])
        for j in range(0, len(urlsSamsung)):
            samsungScreens[samsungName].append(str(mainUrl + urlsSamsung[j]))
            urlsSamsung.remove(urlsSamsung[j])
            break
        break
#-------------------------------------------------------------------------------

# МОНИТОРЫ МСИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_msi.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(msiNames) == 26 and len(urlsMsi) == 26:
        break
    msiNames.append(item.text.strip())
    urlsMsi.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
msiPrices = getPrice(helpArr)
count = 0
while count != 5:
    msiPrices.pop(-1)
    count += 1
helpArr = []
for msiName in msiNames:
    msiScreens[msiName] = []
    for i in range(0, len(msiPrices)):
        msiScreens[msiName].append(msiPrices[i])
        msiPrices.remove(msiPrices[i])
        for j in range(0, len(urlsMsi)):
            msiScreens[msiName].append(str(mainUrl + urlsMsi[j]))
            urlsMsi.remove(urlsMsi[j])
            break
        break
#-------------------------------------------------------------------------------

# МОНИТОРЫ АСУС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_asus.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(asusNames) == 26 and len(urlsAsus) == 26:
        break
    asusNames.append(item.text.strip())
    urlsAsus.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
asusPrices = getPrice(helpArr)
count = 0
while count != 4:
    asusPrices.pop(-1)
    count += 1
helpArr = []
for asusName in asusNames:
    asusScreens[asusName] = []
    for i in range(0, len(asusPrices)):
        asusScreens[asusName].append(asusPrices[i])
        asusPrices.remove(asusPrices[i])
        break
    for j in range(0, len(urlsAsus)):
        asusScreens[asusName].append(str(mainUrl + urlsAsus[j]))
        urlsAsus.remove(urlsAsus[j])
        break
#-------------------------------------------------------------------------------

# МОНИТОРЫ ЛГ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_lg.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(lgNames) == 26 and len(urlsLg) == 26:
        break
    lgNames.append(item.text.strip())
    urlsLg.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
lgPrices = getPrice(helpArr)
count = 0
while count != 8:
    lgPrices.pop(-1)
    count += 1
helpArr = []
for lgName in lgNames:
    lgScreens[lgName] = []
    for i in range(0, len(lgPrices)):
        lgScreens[lgName].append(lgPrices[i])
        lgPrices.remove(lgPrices[i])
        for j in range(0, len(urlsLg)):
            lgScreens[lgName].append(str(mainUrl + urlsLg[j]))
            urlsLg.remove(urlsLg[j])
            break
        break
#--------------------------------------------------------------------------------

# МОНИТОРЫ ДЕЛЛ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_dell.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(dellNames) == 22 and len(urlsDell) == 22:
        break
    dellNames.append(item.text.strip())
    urlsDell.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
dellPrices = getPrice(helpArr)
count = 0
while count != 8:
    dellPrices.pop(-1)
    count += 1
helpArr = []
for dellName in dellNames:
    dellScreens[dellName] = []
    for i in range(0, len(dellPrices)):
        dellScreens[dellName].append(dellPrices[i])
        dellPrices.remove(dellPrices[i])
        for j in range(0, len(urlsDell)):
            dellScreens[dellName].append(str(mainUrl + urlsDell[j]))
            urlsDell.remove(urlsDell[j])
            break
        break
#------------------------------------------------------------------------------

# МОНИТОРЫ БЕНКЬЮ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_benq.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(benqNames) == 26 and len(urlsBenq) == 26:
        break
    benqNames.append(item.text.strip())
    urlsBenq.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
benqPrices = getPrice(helpArr)
count = 0
while count != 8:
    benqPrices.pop(-1)
    count += 1
helpArr = []
for benqName in benqNames:
    benqScreens[benqName] = []
    for i in range(0, len(benqPrices)):
        benqScreens[benqName].append(benqPrices[i])
        benqPrices.remove(benqPrices[i])
        for j in range(0, len(urlsBenq)):
            benqScreens[benqName].append(str(mainUrl + urlsBenq[j]))
            urlsBenq.remove(urlsBenq[j])
            break
        break
#------------------------------------------------------------------------------

# МОНИТОРЫ АОК
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_aoc.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(aocNames) == 26 and len(urlsAoc) == 26:
        break
    aocNames.append(item.text.strip())
    urlsAoc.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
aocPrices = getPrice(helpArr)
count = 0
while count != 4:
    aocPrices.pop(-1)
    count += 1
helpArr = []
for aocName in aocNames:
    aocScreens[aocName] = []
    for i in range(0, len(aocPrices)):
        aocScreens[aocName].append(aocPrices[i])
        aocPrices.remove(aocPrices[i])
        for j in range(0, len(urlsAoc)):
            aocScreens[aocName].append(str(mainUrl + urlsAoc[j]))
            urlsAoc.remove(urlsAoc[j])
            break
        break
#-------------------------------------------------------------------------------

# МОНИТОРЫ ГИГАБАЙТ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_gigabyte.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(gigabyteNames) == 14 and len(urlsGigabyte) == 14:
        break
    gigabyteNames.append(item.text.strip())
    urlsGigabyte.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
gigabytePrices = getPrice(helpArr)
count = 0
while count != 7:
    gigabytePrices.pop(-1)
    count += 1
helpArr = []
for gigabyteName in gigabyteNames:
    gigabyteScreens[gigabyteName] = []
    for i in range(0, len(gigabytePrices)):
        gigabyteScreens[gigabyteName].append(gigabytePrices[i])
        gigabytePrices.remove(gigabytePrices[i])
        for j in range(0, len(urlsGigabyte)):
            gigabyteScreens[gigabyteName].append(str(mainUrl + urlsGigabyte[j]))
            urlsGigabyte.remove(urlsGigabyte[j])
            break
        break
#----------------------------------------------------------------------------------

# МОНИТОРЫ АСЕР
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_acer.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
price = soup.find_all('div', class_ = 'card-price')
index = 0
acerPrices = getPrice(price)
while count != 8:
    acerPrices.pop(-1)
    count += 1
for item in helpArr:
    acerScreens[item.text.strip()] = [acerPrices[index], str(mainUrl + item.get('href'))]
    index += 1
    if index == len(acerPrices):
        break
helpArr = []
# --------------------------------------------------------------------------------

# МОНИТОРЫ АШПИ
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_hp.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(hpNames) == 26 and len(urlsHp) == 26:
        break
    hpNames.append(item.text.strip())
    urlsHp.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
hpPrices = getPrice(helpArr)
count = 0
while count != 8:
    hpPrices.pop(-1)
    count += 1
helpArr = []
for hpName in hpNames:
    hpScreens[hpName] = []
    for i in range(0, len(hpPrices)):
        hpScreens[hpName].append(hpPrices[i])
        hpPrices.remove(hpPrices[i])
        for j in range(0, len(urlsHp)):
            hpScreens[hpName].append(str(mainUrl + urlsHp[j]))
            urlsHp.remove(urlsHp[j])
            break
        break
# ----------------------------------------------------------------------------------

# МОНИТОРЫ ФИЛИПС
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_philips.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
for item in helpArr:
    if len(philipsNames) == 26 and len(urlsPhilips) == 26:
        break
    philipsNames.append(item.text.strip())
    urlsPhilips.append(item.get('href'))
helpArr = []
helpArr = soup.find_all('div', class_ = 'card-price')
philipsPrices = getPrice(helpArr)
count = 0
while count != 7:
    philipsPrices.pop(-1)
    count += 1
helpArr = []
for philipsName in philipsNames:
    philipsScreens[philipsName] = []
    for i in range(0, len(philipsPrices)):
        philipsScreens[philipsName].append(philipsPrices[i])
        philipsPrices.remove(philipsPrices[i])
        for j in range(0, len(urlsPhilips)):
            philipsScreens[philipsName].append(str(mainUrl + urlsPhilips[j]))
            urlsPhilips.remove(urlsPhilips[j])
            break
        break
#----------------------------------------------------------------------------------------

# МОНИТОРЫ ЛЕНОВО
response = requests.get('https://www.foxtrot.com.ua/ru/shop/gk-monitory_lenovo.html')
soup = bs(response.text, 'lxml')
helpArr = soup.find_all('a', class_= 'card__title')
idnex = 0
count = 0
price = soup.find_all('div', class_ = 'card-price')
lenovoPrices = getPrice(price)
while count != 8:
    lenovoPrices.pop(-1)
    count += 1
for i in range(0, len(lenovoPrices)):
    if i == 26:
        break
    lenovoScreens[helpArr[i].text.strip()] = [lenovoPrices[i], (str(mainUrl + helpArr[i].get('href')))]
#---------------------------------------------------------------------------------------