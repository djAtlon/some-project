import requests
import telebot
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs
from phoneModels import createSamsungPhone, createApplePhone, createHuaweiPhone, createMeizuPhone, createOneplusPhone, createOppoPhone, createXiaomiPhone, insertSamsungPhones, insertApplePhones, insertHuaweiPhones, insertMeizuPhones, insertOneplusPhones, insertOppoPhones, insertXiaomiPhones
from tvs import createTvBrands, createSamsungTv, createLgTv, createXiaomiTv, createSonyTv, createPhilipsTv, createToshibaTv, insertTvBrands,insertSamsungTv, insertLgTv, insertXiaomiTv, insertSonyTv, insertPhilipsTv, insertToshibaTv
from tvs import tvBrandsAndStuff, samsungTvs, lgTvs, xiaomiTvs, sonyTvs, philipsTvs, toshibaTvs
from laptops import createLaptopsBrands, createLenovoLaptop, createAsusLaptop, createAcerLaptop, createAppleLaptop, createHpLaptop, createDellLaptop
from laptops import insertLaptopBrands, insertLenovoLaptop, insertAsusLaptop, insertAcerLaptop, insertAppleLaptop, insertHpLaptop, insertDellLaptop
from laptops import laptopBrandsAndAmount, lenovoLaptops, asusLaptops, acerLaptops, macbooks, hpLaptops, dellLaptops
from tablet import createTabletBrands, createSamsungTablet, createLenovoTablet, createAppleTablet, createAlcatelTablet, createHuaweiTablet
from tablet import insertTabletBrands, insertSamsungTablet, insertLenovoTablet, insertAppleTablet, insertAlcatelTablet, insertHuaweiTablet
from tablet import tabletBrandsAndStuff, samsungTablets, lenovoTablets, ipads, alcatelTablets, huaweiTablets
from computer import createComputerProducts, insertComputerProducts, product_names
from screen import createTableScreenBrands, createSamsungScreen, createMsiScreen, createAsusScreen, createLgScreen, createDellScreen, createBenqScreen, createAocScreen, createGigabyteScreen, createAcerScreen, createHpScreen, createPhilipsScreen, createLenovoScreen
from screen import insertScreenBrands, insertSamsungScreen, insertMsiScreen, insertAsusScreen, insertLgScreen, insertDellScreen, insertBenqScreen, insertAocScreen, insertGigabytecreen, insertAcerScreen, insertHpScreen, insertPhilipsScreen, insertLenovoScreen
from screen import screenBrandsAndAmount, samsungScreens, msiScreens, asusScreens, lgScreens, dellScreens, benqScreens, aocScreens, gigabyteScreens, acerScreens, hpScreens, philipsScreens, lenovoScreens
from mouse import createTableMouseBrands, createLogitechMouse, createRazerMouse, createAfourMouse, createHyperxMouse, createSteelSeriesMouse, createAppleMouse, createGeniusMouse, createLenovoMouse
from mouse import insertMouseBrands, insertLogitechMouse, insertRazerMouse, insertAfourMouse, insertHyperxMouse, insertSteelSeriesMouse, insertAppleMouse, insertGeniusMouse, insertLenovoMouse
from mouse import mouseBrandsAndAmount, logitech, razer, a4, hyperx, steel, appleMouses, genius, lenovoMouses
from keyboard import createKeyboardBrands, createLogitechKeyboard, createHyperxKeyboard, createRazerKeyboard, createMsiKeyboard, createAfourTechKeyboard, createAppleKeyboard
from keyboard import insertKeyboardBrands, insertLogitechKeyboard, insertHyperxKeyboard, insertRazerKeyboard, insertMsiKeyboard, insertAfourKeyboard, insertAppleKeyboard
from keyboard import keyboardBrandsAndAmount, logitechKeyboards, hyperxKeyboards, razerKeyboards, msiKeyboards, a4Keyboards, appleKeyboards
from selectFunc import selectCategories

def createConnection(databaseFile):
    connection = None
    try:
        connection = sqlite3.connect(databaseFile)
        return connection
    except Error as error:
        print(error)
    return connection

def createCategoriesTable(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS categories(
                            id int PRIMARY KEY NOT NULL,
                            name text UNIQUE NOT NULL);"""
    
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createProductsTable(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS products(
                            id int PRIMARY KEY NOT NULL,
                            name text UNIQUE NOT NULL,
                            category_id int NOT NULL,
                            FOREIGN KEY (category_id) REFERENCES categories(id));"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_create_table)
    except Error as error:
        print(error)

def createPhonesBrandTable(connection):
    sql_create_table = """CREATE TABLE IF NOT EXISTS phone_brands(
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

def insertCategories(connection, category):
    sql_insert_into_table = """INSERT INTO categories VALUES(?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, category)
        connection.commit()
    except Error as error:
        print(error)


def insertProducts(connection, product):
    sql_insert_into_table = """INSERT INTO products VALUES(?,?,?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, product)
        connection.commit()
    except Error as error:
        print(error)


def insertPhonesBrand(connection, phoneBrand):
    sql_insert_into_table = """INSERT INTO phone_brands VALUES(?, ?, ?, ?);"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql_insert_into_table, phoneBrand)
        connection.commit()
    except Error as error:
        print(error)


def getResponse(url):
    response = requests.get(url)
    return response



def main():
    # databaseFile = r'C:\work\tb\uni\project\some-project\database.db' #work
    databaseFile = r'C:\stuff\uni_course 4\pythonStuff\some-project\database.db' #home
    connection = createConnection(databaseFile)
    mainUrl = 'https://www.foxtrot.com.ua'
    response = getResponse('https://www.foxtrot.com.ua/')
    soup = bs(response.text, 'lxml')
    categories = soup.find_all('li', class_ = 'js-hover-catalog-category') # категории
    phonesAndStuff = [] #телефоны наушники и тд
    laptopsPC = [] #ноутбуки компьютеры планшеты
    tvsAudio = [] #телевизоры и аудиотехника
    forGamers = [] #для геймеров
    phoneBrandAndAmount = {} # для имен брендов телефонов и их кол-ва
    amount = []
    phonesBrand = []

    namesSamsungPhonesAndUrls = []
    samsungPhones = {}
    samsungPhonesPrices = []

    namesIphonesAndUrls = []
    iphones = {}
    iphonesPrice = []

    xiaomiNamesAndUrls = []
    xiaomiPhones = {}
    xiaomiPhonesPrice = []

    oppoNamesAndUrls = []
    oppoPhones = {}
    oppoPhonesPrice = []

    huaweiNamesAndUrls = []
    huaweiPhones = {}
    huaweiPhonesPrice = []

    meizuNamesAndUrls = []
    meizuPhones = {}
    meizuPhonesPrice = []

    oneplusNamesAndUrls = []
    oneplusPhones = {}
    oneplusPhonesPrice = []


    # ТЕЛЕФОНЫ НАУШНИКИ И ПРОЧЕЕ
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-smartfoni-i-telefoni.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion') # вспомогаетльный массив для парсинга всего
    for item in helpArr:
        if item.text.strip() == 'Смартфоны' or item.text.strip() == 'Аксессуары для смартфонов' or item.text.strip() == 'Портативная акустика' or item.text.strip() == 'Наборы для блогеров':
            phonesAndStuff.append(item.text.strip())
    helpArr = [] 
    #--------------------------

    # ТЕХНИКА ДЛЯ КУХНИ
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-tehnika-dlia-kuhni.html')
    soup = bs(response.text, 'lxml')
    kitchenTechs = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    #---------------------------------------------------------------------------------------

    # ТЕХНИКА ДЛЯ ДОМА
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-tehnika-dlia-doma.html')
    soup = bs(response.text, 'lxml')
    homeTechs = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    #------------------------------------------------------------------------------------

    # НОУТБУКИ И ПЛАНШЕТЫ
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-noutbuky-planshety-pk.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    for item in helpArr:
        if item.text.strip() == 'Ноутбуки' or item.text.strip() == 'Планшеты' or item.text.strip() == 'Компьютеры' or item.text.strip() == 'Компьютерная периферия':
            laptopsPC.append(item.text.strip())
    #---------------------------------------------------------------------------
    
    # ТЕЛЕВИЗОРЫ И АУДИОТЕХНИКА
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-televizori-audiotehnika.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    for item in helpArr:
        if item.text.strip() == 'Телевизоры' or item.text.strip() == 'Проекционное оборудование' or item.text.strip() == 'Аудиотехника' or item.text.strip() == 'Аксессуары к телевизорам':
            tvsAudio.append(item.text.strip())
    helpArr = []
    #---------------------------------------------------------------------------


    # ДЛЯ ГЕЙМЕРОВ
    response = getResponse('https://www.foxtrot.com.ua/ru/portal-tovary-dlya-geimerov.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('div', class_ = 'category__item-title js-toggle-accordion')
    for item in helpArr:
        forGamers.append(item.text.strip())
        if len(forGamers) == 8:
            break
    helpArr = []
    # -----------------------------------------------------------------------------''

    # ДЛЯ ИМЕН БРЕНДОВ ТЕЛЕФОНОВ И ИХ КОЛ-ВА
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('label', class_ = 'brand')
    for item in helpArr:
        if item.text.strip() == 'SAMSUNG' or item.text.strip() == 'APPLE' or item.text.strip() == 'XIAOMI' or item.text.strip() =='OPPO' or item.text.strip() == 'HUAWEI' or item.text.strip() == 'MEIZU' or item.text.strip() == 'ONEPLUS':
            phonesBrand.append(item.text.strip())
    helpArr = []
    helpArr = soup.find_all('span', class_ = 'amount')
    for item in helpArr:    
        if item.text.strip().isdigit():
            amount.append(int(item.text))
        if len(amount) == 4:
            break
    amount.append(11)
    amount.append(1)
    amount.append(7)
    helpArr = []
    # new_amount = []
    # for a in amount:
    #     if a == '105':
    #         new_amount.append(int(a))
    #     if a == '147':
    #         new_amount.append(int(a))
    #     if a == '67':
    #         new_amount.append(int(a))
    #     if a == '24':
    #         new_amount.append(int(a))
    #     if a == '10':
    #         new_amount.append(int(a))
    #     if a == '7':
    #         new_amount.append(int(a))
    #         break
    # new_amount.insert(5, 1)
    # # new_amount.remove(1)
    # # new_amount.remove(9)
    # print(len(phonesBrand), phonesBrand)
    # print(len(new_amount), new_amount)
    # print('\n')
    # print(len(phonesBrand), phonesBrand)
    for i in range(0, len(phonesBrand)):
        phoneBrandAndAmount[phonesBrand[i]] = amount[i]
    # --------------------------------------------------------------------


    # ТЕЛЕФОНЫ САМСУНГ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_samsung_smartfon.html')
    soup = bs(response.text, 'lxml')
    namesSamsungPhonesAndUrls = soup.find_all('a', class_ = 'card__title')
    samsungPhonesPrices = soup.find_all('div', class_ = 'card-price')
    for i in range(0, 26):
        samsungPhones[namesSamsungPhonesAndUrls[i].text.strip()] = [int(samsungPhonesPrices[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + namesSamsungPhonesAndUrls[i].get('href'))]
    #----------------------------------------------------------------------------------------------------


    # ТЕЛЕФОНЫ APPLE
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_apple_smartfon.html')
    soup = bs(response.text, 'lxml')
    namesIphonesAndUrls = soup.find_all('a', class_ = 'card__title')
    iphonesPrice = soup.find_all('div', class_ = 'card-price')
    for i in range(0, 26):
        iphones[namesIphonesAndUrls[i].text.strip()] = [int(iphonesPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + namesIphonesAndUrls[i].get('href'))]
    #------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ СЯОМИ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_xiaomi_smartfon.html')
    soup = bs(response.text, 'lxml')
    xiaomiNamesAndUrls = soup.find_all('a', class_ = 'card__title')
    xiaomiPhonesPrice = soup.find_all('div', class_ = 'card-price')
    for i in range(0, 26):
        xiaomiPhones[xiaomiNamesAndUrls[i].text.strip()] = [int(xiaomiPhonesPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + xiaomiNamesAndUrls[i].get('href'))]
    #--------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ ОППО
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_oppo_smartfon.html')
    soup = bs(response.text, 'lxml')
    oppoNamesAndUrls  = soup.find_all('a', class_ = 'card__title')
    oppoPhonesPrice  = soup.find_all('div', class_ = 'card-price')
    for i in range(0, 23):
        oppoPhones[oppoNamesAndUrls[i].text.strip()] = [int(oppoPhonesPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + oppoNamesAndUrls[i].get('href'))]
    #------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ ХУАВЕЙ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_huawei_smartfon.html')
    soup = bs(response.text, 'lxml')
    huaweiNamesAndUrls = soup.find_all('a', class_ = 'card__title')
    huaweiPhonesPrice = soup.find_all('div', class_ = 'card-price')
    for i in range(0, 10):
        huaweiPhones[huaweiNamesAndUrls[i].text.strip()] = [int(huaweiPhonesPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + huaweiNamesAndUrls[i].get('href'))]
    #--------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ МЕЙЗУ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_meizu_smartfon.html')
    soup = bs(response.text, 'lxml')
    meizuNamesAndUrls = soup.find_all('a', class_ = 'card__title')
    meizuPhonesPrice = soup.find_all('div', class_ = 'card-price')
    for i in range(0, 1):
        meizuPhones[meizuNamesAndUrls[i].text.strip()] = [int(meizuPhonesPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + meizuNamesAndUrls[i].get('href'))]
    #--------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ ВАНПЛЮС
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_oneplus_smartfon.html')
    soup = bs(response.text, 'lxml')
    oneplusNamesAndUrls = soup.find_all('a', class_ = 'card__title')
    oneplusPhonesPrice = soup.find_all('div', 'card-price')
    for i in range(0, 6):
        oneplusPhones[oneplusNamesAndUrls[i].text.strip()] = [int(oneplusPhonesPrice[i].text.strip().replace(' ', '').split('₴')[0]), str(mainUrl + oneplusNamesAndUrls[i].get('href'))]
    # ---------------------------------------------------------------------------------------------------


    # with connection:
    #     createCategoriesTable(connection)
    #     createProductsTable(connection)
    #     createPhonesBrandTable(connection)
    #     for categoryId, category in enumerate(categories, start=1):
    #         c = (categoryId, category.text.strip())
    #         insertCategories(connection, c)

    #     for phoneAndStuffId, phoneAndStuff in enumerate(phonesAndStuff, start=1):
    #         p = (phoneAndStuffId, phoneAndStuff, 1)
    #         insertProducts(connection, p)
    #     for tvId, tvAudio in enumerate(tvsAudio, start=5):
    #         t = (tvId, tvAudio, 2)
    #         insertProducts(connection, t)
    #     for kitchenId, kitchenTech in enumerate(kitchenTechs, start=9):
    #         k = (kitchenId, kitchenTech.text.strip(), 3)
    #         insertProducts(connection, k)
    #     for homeId, homeTech in enumerate(homeTechs, start=17):
    #         h = (homeId, homeTech.text.strip(), 4)
    #         insertProducts(connection, h)
    #     for laptopPCId, laptopPC in enumerate(laptopsPC, start=25):
    #         l = (laptopPCId, laptopPC, 5)
    #         insertProducts(connection, l)
    #     for gamingId, forGamer in enumerate(forGamers, start=29):
    #         g = (gamingId, forGamer, 6)
    #         insertProducts(connection, g)

    #     for index, phone in enumerate(phoneBrandAndAmount, start=1):
    #         p = (index, phone, phoneBrandAndAmount.get(phone), 1)
    #         insertPhonesBrand(connection, p)
    
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ МОДЕЛЕЙ ТЕЛЕФОНОВ
    # with connection:
    #     createSamsungPhone(connection)
    #     createApplePhone(connection)
    #     createXiaomiPhone(connection)
    #     createOppoPhone(connection)
    #     createHuaweiPhone(connection)
    #     createMeizuPhone(connection)
    #     createOneplusPhone(connection)
    #     for samsungPhoneId, samsungPhone in enumerate(samsungPhones, start=1):
    #         s = (samsungPhoneId, samsungPhone, samsungPhones.get(samsungPhone)[0], 1, samsungPhones.get(samsungPhone)[1])
    #         insertSamsungPhones(connection, s)
    #     for iphoneId, iphone in enumerate(iphones, start=1):
    #         i = (iphoneId, iphone, iphones.get(iphone)[0], 2, iphones.get(iphone)[1])
    #         insertApplePhones(connection, i)
    #     for xiaomiPhoneId, xiaomiPhone in enumerate(xiaomiPhones, start=1):
    #         x = (xiaomiPhoneId, xiaomiPhone, xiaomiPhones.get(xiaomiPhone)[0], 3, xiaomiPhones.get(xiaomiPhone)[1])
    #         insertXiaomiPhones(connection, x)
    #     for oppoPhoneId, oppoPhone in enumerate(oppoPhones, start=1):
    #         oppo = (oppoPhoneId, oppoPhone, oppoPhones.get(oppoPhone)[0], 4, oppoPhones.get(oppoPhone)[1])
    #         insertOppoPhones(connection, oppo)
    #     for huaweiId, huaweiPhone in enumerate(huaweiPhones, start=1):
    #         h = (huaweiId, huaweiPhone, huaweiPhones.get(huaweiPhone)[0], 5, huaweiPhones.get(huaweiPhone)[1])
    #         insertHuaweiPhones(connection, h)
    #     for meizuId, meizuPhone in enumerate(meizuPhones, start=1):
    #         m = (meizuId, meizuPhone, meizuPhones.get(meizuPhone)[0], 6, meizuPhones.get(meizuPhone)[1])
    #         insertMeizuPhones(connection, m)
    #     for oneplusId, oneplusPhone in enumerate(oneplusPhones, start=1):
    #         oneplus = (oneplusId, oneplusPhone, oneplusPhones.get(oneplusPhone)[0], 7, oneplusPhones.get(oneplusPhone)[1])
    #         insertOneplusPhones(connection, oneplus)
    # #-----------------------------------------
    # # for t in tvBrandsAndStuff:
    # #     print(tvBrandsAndStuff.get(t)[0])
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ МОДЕЛЕЙ ТЕЛЕВИЗОРОВ
    # with connection:
    #     createTvBrands(connection)
    #     createSamsungTv(connection)
    #     createLgTv(connection)
    #     createXiaomiTv(connection)
    #     createSonyTv(connection)
    #     createPhilipsTv(connection)
    #     createToshibaTv(connection)
    #     for tvBrandId, tvBrand in enumerate(tvBrandsAndStuff, start=1):
    #         t = (tvBrandId, tvBrand, tvBrandsAndStuff.get(tvBrand), 5)
    #         insertTvBrands(connection, t)
    #     for samsungTvId, samsungTv in enumerate(samsungTvs, start=1):
    #         s = (samsungTvId, samsungTv, samsungTvs.get(samsungTv)[0], 1, samsungTvs.get(samsungTv)[1])
    #         insertSamsungTv(connection, s)
    #     for lgTvId, lgTv in enumerate(lgTvs, start=1):
    #         l = (lgTvId, lgTv, lgTvs.get(lgTv)[0], 2, lgTvs.get(lgTv)[1])
    #         insertLgTv(connection, l)
    #     for xaiomiTvId, xiaomiTv in enumerate(xiaomiTvs, start=1):
    #         x = (xaiomiTvId, xiaomiTv, xiaomiTvs.get(xiaomiTv)[0], 3, xiaomiTvs.get(xiaomiTv)[1])
    #         insertXiaomiTv(connection, x)
    #     for sonyTvId, sonyTv in enumerate(sonyTvs, start=1):
    #         s = (sonyTvId, sonyTv, sonyTvs.get(sonyTv)[0], 4, sonyTvs.get(sonyTv)[1])
    #         insertSonyTv(connection, s)
    #     for philipsTvId, philipsTv in enumerate(philipsTvs, start=1):
    #         p = (philipsTvId, philipsTv, philipsTvs.get(philipsTv)[0], 5, philipsTvs.get(philipsTv)[1])
    #         insertPhilipsTv(connection, p)
    #     for toshibaTvId, toshibaTv in enumerate(toshibaTvs, start=1):
    #         t = (toshibaTvId, toshibaTv, toshibaTvs.get(toshibaTv)[0], 6, toshibaTvs.get(toshibaTv)[1])
    #         insertToshibaTv(connection, t)
    
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ МОДЕЛЕЙ НОУТБУКОВ
    # with connection:
    #     createLaptopsBrands(connection)
    #     createLenovoLaptop(connection)
    #     createAsusLaptop(connection)
    #     createAcerLaptop(connection)
    #     createAppleLaptop(connection)
    #     createHpLaptop(connection)
    #     createDellLaptop(connection)
    #     for laptopBrandId, laptopBrand in enumerate(laptopBrandsAndAmount, start=1):
    #         l = (laptopBrandId, laptopBrand, laptopBrandsAndAmount.get(laptopBrand), 25)
    #         insertLaptopBrands(connection, l)
    #     for lenovoId, lenovoLaptop in enumerate(lenovoLaptops, start=1):
    #         l = (lenovoId, lenovoLaptop, lenovoLaptops.get(lenovoLaptop)[0], 1, lenovoLaptops.get(lenovoLaptop)[1])
    #         insertLenovoLaptop(connection, l)
    #     for asusId, asusLaptop in enumerate(asusLaptops, start=1):
    #         a = (asusId, asusLaptop, asusLaptops.get(asusLaptop)[0], 2, asusLaptops.get(asusLaptop)[1])
    #         insertAsusLaptop(connection, a)
    #     for acerId, acerLaptop in enumerate(acerLaptops, start=1):
    #         a = (acerId, acerLaptop, acerLaptops.get(acerLaptop)[0], 3, acerLaptops.get(acerLaptop)[1])
    #         insertAcerLaptop(connection, a)
    #     for macbookId, macbook in enumerate(macbooks, start=1):
    #         m = (macbookId, macbook, macbooks.get(macbook)[0], 4, macbooks.get(macbook)[1])
    #         insertAppleLaptop(connection, m)
    #     for hpId, hpLaptop in enumerate(hpLaptops, start=1):
    #         h = (hpId, hpLaptop, hpLaptops.get(hpLaptop)[0], 5, hpLaptops.get(hpLaptop)[1])
    #         insertHpLaptop(connection, h)
    #     for dellId, dellLaptop in enumerate(dellLaptops, start=1):
    #         d = (dellId, dellLaptop, dellLaptops.get(dellLaptop)[0], 6, dellLaptops.get(dellLaptop)[1])
    #         insertDellLaptop(connection, d)
    
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ ПЛАНШЕТОВ
    # with connection:
    #     createTabletBrands(connection)
    #     createSamsungTablet(connection)
    #     createLenovoTablet(connection)
    #     createAppleTablet(connection)
    #     createAlcatelTablet(connection)
    #     createHuaweiTablet(connection)
    #     for tabletBrandId, tabletBrand in enumerate(tabletBrandsAndStuff, start=1):
    #         t = (tabletBrandId, tabletBrand, tabletBrandsAndStuff.get(tabletBrand), 26)
    #         insertTabletBrands(connection, t)
    #     for samsungId, samsungTablet in enumerate(samsungTablets, start=1):
    #         s = (samsungId, samsungTablet, samsungTablets.get(samsungTablet)[0], 1, samsungTablets.get(samsungTablet)[1])
    #         insertSamsungTablet(connection, s)
    #     for lenovoId, lenovoTablet in enumerate(lenovoTablets, start=1):
    #         l = (lenovoId, lenovoTablet, lenovoTablets.get(lenovoTablet)[0], 2, lenovoTablets.get(lenovoTablet)[1])
    #         insertLenovoTablet(connection, l)
    #     for ipadId, ipad in enumerate(ipads, start=1):
    #         i = (ipadId, ipad, ipads.get(ipad)[0], 3, ipads.get(ipad)[1])
    #         insertAppleTablet(connection, i)
    #     for alcatelId, alcatelName in enumerate(alcatelTablets, start=1):
    #         a = (alcatelId, alcatelName, alcatelTablets.get(alcatelName)[0], 4, alcatelTablets.get(alcatelName)[1])
    #         insertAlcatelTablet(connection, a)
    #     for huaweiId, huaweiName in enumerate(huaweiTablets, start=1):
    #         h = (huaweiId, huaweiName, huaweiTablets.get(huaweiName)[0], 5, huaweiTablets.get(huaweiName)[1])
    #         insertHuaweiTablet(connection, h)
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ ПРОДУКТОВ КОМПЬЮТЕРНОЙ ПЕРИФЕРИИ
    # with connection:
    #     createComputerProducts(connection)
    #     for computerProductId, computerProduct in enumerate(product_names, start=1):
    #         c = (computerProductId, computerProduct, 28)
    #         insertComputerProducts(connection, c)
    
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ БРЕНДОВ МОНИТОРОВ
    # with connection:
    #     createTableScreenBrands(connection)
    #     createSamsungScreen(connection)
    #     createMsiScreen(connection)
    #     createAsusScreen(connection)
    #     createLgScreen(connection)
    #     createDellScreen(connection)
    #     createBenqScreen(connection)
    #     createAocScreen(connection)
    #     createGigabyteScreen(connection)
    #     createAcerScreen(connection)
    #     createHpScreen(connection)
    #     createPhilipsScreen(connection)
    #     createLenovoScreen(connection)
    #     for screenBrandId, screenBrand in enumerate(screenBrandsAndAmount, start=1):
    #         s = (screenBrandId, screenBrand, screenBrandsAndAmount.get(screenBrand))
    #         insertScreenBrands(connection, s)
    #     for samsungScreenId, samsungScreen in enumerate(samsungScreens, start=1):
    #         s = (samsungScreenId, samsungScreen, samsungScreens.get(samsungScreen)[0], samsungScreens.get(samsungScreen)[1])
    #         insertSamsungScreen(connection, s)
    #     for msiId, msi in enumerate(msiScreens, start=1):
    #         m = (msiId, msi, msiScreens.get(msi)[0], msiScreens.get(msi)[1])
    #         insertMsiScreen(connection, m)
    #     for asusId, asus in enumerate(asusScreens, start=1):
    #         a = (asusId, asus, asusScreens.get(asus)[0], asusScreens.get(asus)[1])
    #         insertAsusScreen(connection, a)
    #     for lgId, lg in enumerate(lgScreens, start=1):
    #         l = (lgId, lg, lgScreens.get(lg)[0], lgScreens.get(lg)[1])
    #         insertLgScreen(connection, l)
    #     for dellId, dell in enumerate(dellScreens, start=1):
    #         d = (dellId, dell, dellScreens.get(dell)[0], dellScreens.get(dell)[1])
    #         insertDellScreen(connection, d)
    #     for benqId, benq in enumerate(benqScreens, start=1):
    #         b = (benqId, benq, benqScreens.get(benq)[0], benqScreens.get(benq)[1])
    #         insertBenqScreen(connection, b)
    #     for aocId, aoc in enumerate(aocScreens, start=1):
    #         a = (aocId, aoc, aocScreens.get(aoc)[0], aocScreens.get(aoc)[1])
    #         insertAocScreen(connection, a)
    #     for gigabyteId, gigabyte in enumerate(gigabyteScreens, start=1):
    #         g = (gigabyteId, gigabyte, gigabyteScreens.get(gigabyte)[0], gigabyteScreens.get(gigabyte)[1])
    #         insertGigabytecreen(connection, g)
    #     for acerId, acer in enumerate(acerScreens, start=1):
    #         a = (acerId, acer, acerScreens.get(acer)[0], acerScreens.get(acer)[1])
    #         insertAcerScreen(connection, a)
    #     for hpId, hp in enumerate(hpScreens, start=1):
    #         h = (hpId, hp, hpScreens.get(hp)[0], hpScreens.get(hp)[1])
    #         insertHpScreen(connection, h)
    #     for philipsId, philips in enumerate(philipsScreens, start=1):
    #         p = (philipsId, philips, philipsScreens.get(philips)[0], philipsScreens.get(philips)[1])
    #         insertPhilipsScreen(connection, p)
    #     for lenovoId, lenovo in enumerate(lenovoScreens, start=1):
    #         l = (lenovoId, lenovo, lenovoScreens.get(lenovo)[0], lenovoScreens.get(lenovo)[1])
    #         insertLenovoScreen(connection, l)

    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ БРЕНДОВ КОМП МЫШЕЙ
    # with connection:
    #     createTableMouseBrands(connection)
    #     createLogitechMouse(connection)
    #     createRazerMouse(connection)
    #     createAfourMouse(connection)
    #     createHyperxMouse(connection)
    #     createSteelSeriesMouse(connection)
    #     createAppleMouse(connection)
    #     createGeniusMouse(connection)
    #     createLenovoMouse(connection)
    #     for mouseBrandId, mouseBrand in enumerate(mouseBrandsAndAmount, start=1):
    #         m = (mouseBrandId, mouseBrand, mouseBrandsAndAmount.get(mouseBrand))
    #         insertMouseBrands(connection, m)
    #     for logitechId, logitechName in enumerate(logitech, start=1):
    #         l = (logitechId, logitechName, logitech.get(logitechName)[0], logitech.get(logitechName)[1])
    #         insertLogitechMouse(connection, l)
    #     for razerId, razerName in enumerate(razer, start=1):
    #         r = (razerId, razerName, razer.get(razerName)[0],razer.get(razerName)[1])
    #         insertRazerMouse(connection, r)
    #     for aId, aName in enumerate(a4, start=1):
    #         a = (aId, aName, a4.get(aName)[0], a4.get(aName)[1])
    #         insertAfourMouse(connection, a)
    #     for hyperxId, hyperxName in enumerate(hyperx, start=1):
    #         h = (hyperxId, hyperxName, hyperx.get(hyperxName)[0], hyperx.get(hyperxName)[1])
    #         insertHyperxMouse(connection, h)
    #     for steelId, steelName in enumerate(steel, start=1):
    #         s = (steelId, steelName, steel.get(steelName)[0], steel.get(steelName)[1])
    #         insertSteelSeriesMouse(connection, s)
    #     for appleMouseId, appleMouseName in enumerate(appleMouses, start=1):
    #         a = (appleMouseId, appleMouseName, appleMouses.get(appleMouseName)[0], appleMouses.get(appleMouseName)[1])
    #         insertAppleMouse(connection, a)
    #     for geniusId, geniusMouse in enumerate(genius, start=1):
    #         g = (geniusId, geniusMouse, genius.get(geniusMouse)[0], genius.get(geniusMouse)[1])
    #         insertGeniusMouse(connection, g)
    #     for lenovoMouseId, lenovoMouse in enumerate(lenovoMouses, start=1):
    #         l = (lenovoMouseId, lenovoMouse, lenovoMouses.get(lenovoMouse)[0], lenovoMouses.get(lenovoMouse)[1])
    #         insertLenovoMouse(connection, l)
    
    # # СОЗДАНИЕ ТАБЛИЦ ДЛЯ БРЕНДОВ КЛАВИАТУР
    # with connection:
    #     createKeyboardBrands(connection)
    #     createLogitechKeyboard(connection)
    #     createHyperxKeyboard(connection)
    #     createRazerKeyboard(connection)
    #     createMsiKeyboard(connection)
    #     createAfourTechKeyboard(connection)
    #     createAppleKeyboard(connection)
    #     for keyboardBrandId, keyboardBrand in enumerate(keyboardBrandsAndAmount, start=1):
    #         k = (keyboardBrandId, keyboardBrand, keyboardBrandsAndAmount.get(keyboardBrand))
    #         insertKeyboardBrands(connection, k)
    #     for logitechKeyboardId, logitechKeyboard in enumerate(logitechKeyboards, start=1):
    #         l = (logitechKeyboardId, logitechKeyboard, logitechKeyboards.get(logitechKeyboard)[0], logitechKeyboards.get(logitechKeyboard)[1])
    #         insertLogitechKeyboard(connection, l)
    #     for hyperxKeyboardId, hyperxKeyboard in enumerate(hyperxKeyboards, start=1):
    #         h = (hyperxKeyboardId, hyperxKeyboard, hyperxKeyboards.get(hyperxKeyboard)[0], hyperxKeyboards.get(hyperxKeyboard)[1])
    #         insertHyperxKeyboard(connection, h)
    #     for razerKeyboardId, razerKeyboard in enumerate(razerKeyboards, start=1):
    #         r = (razerKeyboardId, razerKeyboard, razerKeyboards.get(razerKeyboard)[0], razerKeyboards.get(razerKeyboard)[1])
    #         insertRazerKeyboard(connection, r)
    #     for msiKeyboardId, msiKeyboard in enumerate(msiKeyboards, start=1):
    #         m =  (msiKeyboardId, msiKeyboard, msiKeyboards.get(msiKeyboard)[0], msiKeyboards.get(msiKeyboard)[1])
    #         insertMsiKeyboard(connection, m)
    #     for aKeyboardId, aKeyboard in enumerate(a4Keyboards, start=1):
    #         a = (aKeyboardId, aKeyboard, a4Keyboards.get(aKeyboard)[0], a4Keyboards.get(aKeyboard)[1])
    #         insertAfourKeyboard(connection, a)
    #     for appleKeyboardId, appleKeyboard in enumerate(appleKeyboards, start=1):
    #         a = (appleKeyboardId, appleKeyboard, appleKeyboards.get(appleKeyboard)[0], appleKeyboards.get(appleKeyboard)[1])
    #         insertAppleKeyboard(connection, a)
    # #-----------------------------------------------------------------------------------------------------------------------

    # with connection:
    #     showCategories = selectCategories(connection)
    #     for showCategory in showCategories:
    #         print(str(showCategory))


if __name__ == '__main__':
    main()