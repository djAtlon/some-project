from sqlite3.dbapi2 import connect
import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup as bs
from requests.models import cookiejar_from_dict
from phoneModels import createSamsungPhone, createApplePhone, createHuaweiPhone, createMeizuPhone, createOneplusPhone, createOppoPhone, createXiaomiPhone, insertSamsungPhones, insertApplePhones, insertHuaweiPhones, insertMeizuPhones, insertOneplusPhones, insertOppoPhones, insertXiaomiPhones
from tvs import createTvBrands, createSamsungTv, createLgTv, createXiaomiTv, createSonyTv, createPhilipsTv, createToshibaTv, insertTvBrands,insertSamsungTv, insertLgTv, insertXiaomiTv, insertSonyTv, insertPhilipsTv, insertToshibaTv
from tvs import tvBrandsAndStuff, samsungTvs, lgTvs, xiaomiTvs, sonyTvs, philipsTvs, toshibaTvs
from laptops import createLaptopsBrands, createLenovoLaptop, createAsusLaptop, createAcerLaptop, createAppleLaptop, createHpLaptop, createDellLaptop
from laptops import insertLaptopBrands, insertLenovoLaptop, insertAsusLaptop, insertAcerLaptop, insertAppleLaptop, insertHpLaptop, insertDellLaptop
from laptops import laptopBrandsAndAmount, lenovoLaptops, asusLaptops, acerLaptops, macbooks, hpLaptops, dellLaptops
from tablet import createTabletBrands, createSamsungTablet, createLenovoTablet, createAppleTablet, createAlcatelTablet, createHuaweiTablet
from tablet import insertTabletpBrands, insertSamsungTablet, insertLenovoTablet, insertAppleTablet, insertAlcatelTablet, insertHuaweiTablet
from tablet import tabletBrandsAndStuff, samsungTablets, lenovoTablets, ipads, alcatelTablets, huaweiTablets

def returnPrice(helpArr):
    priceArr = []
    for item in helpArr:
        price = item.text.strip()
        new_price = price.split('₴')[0]
        firstPart = new_price.split(' ')[0]
        secondPart = new_price.split(' ')[1]
        priceArr.append(int(firstPart + secondPart))
    return priceArr



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
    databaseFile = r'C:\work\tb\uni\project\some-project\database.db'
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

    namesSamsungPhones = []
    urlsSamsungPhones = []
    samsungPhones = {}
    samsungPhonesPrices = []

    namesIphones = []
    urlsIphones = []
    iphones = {}
    iphonesPrice = []

    xiaomiNames = []
    urlsXiaomi = []
    xiaomiPhones = {}
    xiaomiPhonesPrice = []

    oppoNames = []
    urlsOppo = []
    oppoPhones = {}
    oppoPhonesPrice = []

    huaweiNames = []
    urlsHuawei = []
    huaweiPhones = {}
    huaweiPhonesPrice = []

    meizuNames = []
    urlsMeizu = []
    meizuPhones = {}
    meizuPhonesPrice = []

    oneplusNames = []
    urlsOneplus = []
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
        amount.append(item.text.strip())
        if len(amount) == 20:
            break
    helpArr = []
    new_amount = []
    for a in amount:
        if a == '103':
            new_amount.append(int(a))
        if a == '148':
            new_amount.append(int(a))
        if a == '66':
            new_amount.append(int(a))
        if a == '26':
            new_amount.append(int(a))
        if a == '10':
            new_amount.append(int(a))
        if a == '7':
            new_amount.append(int(a))
            break
    # new_amount.insert(5, 1)
    # # new_amount.remove(1)
    # # new_amount.remove(9)
    # print(len(phonesBrand), phonesBrand)
    # print(len(new_amount), new_amount)
    # print('\n')
    # print(len(phonesBrand), phonesBrand)
    for i in range(0, len(phonesBrand)):
        phoneBrandAndAmount[phonesBrand[i]] = new_amount[i]
    # --------------------------------------------------------------------


    # ТЕЛЕФОНЫ САМСУНГ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_samsung_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        namesSamsungPhones.append(item.text.strip())
        urlsSamsungPhones.append(item.get('href'))
    helpArr = []
    helpArr = soup.find_all('div', class_ = 'card-price')
    samsungPhonesPrices = returnPrice(helpArr)
    helpArr = []
    for nameSamgungPhone in namesSamsungPhones:
        samsungPhones[nameSamgungPhone] = []
        for i in range(0, len(samsungPhonesPrices)):
            samsungPhones[nameSamgungPhone].append(samsungPhonesPrices[i])
            samsungPhonesPrices.remove(samsungPhonesPrices[i])
            for j in range(0, len(urlsSamsungPhones)):
                samsungPhones[nameSamgungPhone].append(str(mainUrl + urlsSamsungPhones[j]))
                urlsSamsungPhones.remove(urlsSamsungPhones[j])
                break
            break
    #----------------------------------------------------------------------------------------------------


    # ТЕЛЕФОНЫ APPLE
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_apple_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        namesIphones.append(item.text.strip())
        urlsIphones.append(item.get('href'))
    helpArr = []
    helpArr = soup.find_all('div', class_ = 'card-price')
    iphonesPrice = returnPrice(helpArr)
    helpArr = []
    for iphoneName in namesIphones:
        iphones[iphoneName] = []
        for i in range(0, len(iphonesPrice)):
            iphones[iphoneName].append(iphonesPrice[i])
            iphonesPrice.remove(iphonesPrice[i])
            for j in range(0, len(urlsIphones)):
                iphones[iphoneName].append(str(mainUrl + urlsIphones[j]))
                urlsIphones.remove(urlsIphones[j])
                break
            break
    #------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ СЯОМИ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_xiaomi_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        xiaomiNames.append(item.text.strip())
        urlsXiaomi.append(item.get('href'))
    helpArr = []
    helpArr = soup.find_all('div', class_ = 'card-price')
    xiaomiPhonesPrice = returnPrice(helpArr)
    helpArr = []
    for xiaomiName in xiaomiNames:
        xiaomiPhones[xiaomiName] = []
        for i in range(0, len(xiaomiPhonesPrice)):
            xiaomiPhones[xiaomiName].append(xiaomiPhonesPrice[i])
            xiaomiPhonesPrice.remove(xiaomiPhonesPrice[i])
            for j in range(0, len(urlsXiaomi)):
                xiaomiPhones[xiaomiName].append(str(mainUrl + urlsXiaomi[j]))
                urlsXiaomi.remove(urlsXiaomi[j])
                break
            break
    #--------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ ОППО
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_oppo_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        oppoNames.append(item.text.strip())
        urlsOppo.append(item.get('href'))
    helpArr = []
    helpArr = soup.find_all('div', class_ = 'card-price')
    oppoPhonesPrice = returnPrice(helpArr)
    helpArr = []
    for oppoName in oppoNames:
        oppoPhones[oppoName] = []
        for i in range(0, len(oppoPhonesPrice)):
            oppoPhones[oppoName].append(oppoPhonesPrice[i])
            oppoPhonesPrice.remove(oppoPhonesPrice[i])
            for j in range(0, len(urlsOppo)):
                oppoPhones[oppoName].append(str(mainUrl + urlsOppo[j]))
                urlsOppo.remove(urlsOppo[j])
                break
            break
    #------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ ХУАВЕЙ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_huawei_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        huaweiNames.append(item.text.strip())
        urlsHuawei.append(item.get('href'))
        if len(huaweiNames) == 10:
            break
        if len(urlsHuawei) == 10:
            break
    helpArr = []
    helpArr = soup.find_all('div', class_ = 'card-price')
    huaweiPhonesPrice = returnPrice(helpArr)
    helpArr = []
    for huaweiName in huaweiNames:
        huaweiPhones[huaweiName] = []
        for i in range(0, len(huaweiPhonesPrice)):
            huaweiPhones[huaweiName].append(huaweiPhonesPrice[i])
            huaweiPhonesPrice.remove(huaweiPhonesPrice[i])
            for j in range(0, len(urlsHuawei)):
                huaweiPhones[huaweiName].append(str(mainUrl + urlsHuawei[j]))
                urlsHuawei.remove(urlsHuawei[j])
                break
            break
    
    #--------------------------------------------------------------------------------------------------

    # ТЕЛЕФОНЫ МЕЙЗУ
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_meizu_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        meizuNames.append(item.text.strip())
        urlsMeizu.append(item.get('href'))
        if len(meizuNames) == 1 and len(urlsMeizu):
            break
    helpArr = []
    helpArr = soup.find_all('div', class_ = 'card-price')
    meizuPhonesPrice = returnPrice(helpArr)
    helpArr = []
    for meizuName in meizuNames:
        meizuPhones[meizuName] = []
        for i in range(0, len(meizuPhonesPrice)):
            meizuPhones[meizuName].append(meizuPhonesPrice[i])
            for j in range(0, len(urlsMeizu)):
                meizuPhones[meizuName].append(str(mainUrl + urlsMeizu[j]))
                break
            break
    #--------------------------------------------------------------------------------------------------
    
    






    # ТЕЛЕФОНЫ ВАНПЛЮС
    response = getResponse('https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_oneplus_smartfon.html')
    soup = bs(response.text, 'lxml')
    helpArr = soup.find_all('a', class_ = 'card__title')
    for item in helpArr:
        oneplusNames.append(item.text.strip())
        urlsOneplus.append(item.get('href'))
    helpArr = []
    helpArr = soup.find_all('div', 'card-price')
    oneplusPhonesPrice = returnPrice(helpArr)
    for oneplusName in oneplusNames:
        oneplusPhones[oneplusName] = []
        for i in range(0, len(oneplusPhonesPrice)):
            oneplusPhones[oneplusName].append(oneplusPhonesPrice[i])
            oneplusPhonesPrice.remove(oneplusPhonesPrice[i])
            for j in range(0, len(urlsOneplus)):
                oneplusPhones[oneplusName].append(urlsOneplus[j])
                urlsOneplus.remove(urlsOneplus[j])
                break
            break
    # ---------------------------------------------------------------------------------------------------




    with connection:
        createCategoriesTable(connection)
        createProductsTable(connection)
        createPhonesBrandTable(connection)
        for categoryId, category in enumerate(categories, start=1):
            c = (categoryId, category.text.strip())
            insertCategories(connection, c)

        for phoneAndStuffId, phoneAndStuff in enumerate(phonesAndStuff, start=1):
            p = (phoneAndStuffId, phoneAndStuff, 1)
            insertProducts(connection, p)
        for tvId, tvAudio in enumerate(tvsAudio, start=5):
            t = (tvId, tvAudio, 2)
            insertProducts(connection, t)
        for kitchenId, kitchenTech in enumerate(kitchenTechs, start=9):
            k = (kitchenId, kitchenTech.text.strip(), 3)
            insertProducts(connection, k)
        for homeId, homeTech in enumerate(homeTechs, start=17):
            h = (homeId, homeTech.text.strip(), 4)
            insertProducts(connection, h)
        for laptopPCId, laptopPC in enumerate(laptopsPC, start=25):
            l = (laptopPCId, laptopPC, 5)
            insertProducts(connection, l)
        for gamingId, forGamer in enumerate(forGamers, start=29):
            g = (gamingId, forGamer, 6)
            insertProducts(connection, g)

        for index, phone in enumerate(phoneBrandAndAmount, start=1):
            p = (index, phone, phoneBrandAndAmount.get(phone), 1)
            insertPhonesBrand(connection, p)
    
    # СОЗДАНИЕ ТАБЛИЦ ДЛЯ МОДЕЛЕЙ ТЕЛЕФОНОВ
    with connection:
        createSamsungPhone(connection)
        createApplePhone(connection)
        createXiaomiPhone(connection)
        createOppoPhone(connection)
        createHuaweiPhone(connection)
        createMeizuPhone(connection)
        createOneplusPhone(connection)
        for samsungPhoneId, samsungPhone in enumerate(samsungPhones, start=1):
            s = (samsungPhoneId, samsungPhone, samsungPhones.get(samsungPhone)[0], 1, samsungPhones.get(samsungPhone)[1])
            insertSamsungPhones(connection, s)
        for iphoneId, iphone in enumerate(iphones, start=1):
            i = (iphoneId, iphone, iphones.get(iphone)[0], 2, iphones.get(iphone)[1])
            insertApplePhones(connection, i)
        for xiaomiPhoneId, xiaomiPhone in enumerate(xiaomiPhones, start=1):
            x = (xiaomiPhoneId, xiaomiPhone, xiaomiPhones.get(xiaomiPhone)[0], 3, xiaomiPhones.get(xiaomiPhone)[1])
            insertXiaomiPhones(connection, x)
        for oppoPhoneId, oppoPhone in enumerate(oppoPhones, start=1):
            oppo = (oppoPhoneId, oppoPhone, oppoPhones.get(oppoPhone)[0], 4, oppoPhones.get(oppoPhone)[1])
            insertOppoPhones(connection, oppo)
        for huaweiId, huaweiPhone in enumerate(huaweiPhones, start=1):
            h = (huaweiId, huaweiPhone, huaweiPhones.get(huaweiPhone)[0], 5, huaweiPhones.get(huaweiPhone)[1])
            insertHuaweiPhones(connection, h)
        for meizuId, meizuPhone in enumerate(meizuPhones, start=1):
            m = (meizuId, meizuPhone, meizuPhones.get(meizuPhone)[0], 6, meizuPhones.get(meizuPhone)[1])
            insertMeizuPhones(connection, m)
        for oneplusId, oneplusPhone in enumerate(oneplusPhones, start=1):
            oneplus = (oneplusId, oneplusPhone, oneplusPhones.get(oneplusPhone)[0], 7, oneplusPhones.get(oneplusPhone)[1])
            insertOneplusPhones(connection, oneplus)
    #-----------------------------------------
    # for t in tvBrandsAndStuff:
    #     print(tvBrandsAndStuff.get(t)[0])
    # СОЗДАНИЕ ТАБЛИЦ ДЛЯ МОДЕЛЕЙ ТЕЛЕВИЗОРОВ
    with connection:
        createTvBrands(connection)
        createSamsungTv(connection)
        createLgTv(connection)
        createXiaomiTv(connection)
        createSonyTv(connection)
        createPhilipsTv(connection)
        createToshibaTv(connection)
        for tvBrandId, tvBrand in enumerate(tvBrandsAndStuff, start=1):
            t = (tvBrandId, tvBrand, tvBrandsAndStuff.get(tvBrand), 5)
            insertTvBrands(connection, t)
        for samsungTvId, samsungTv in enumerate(samsungTvs, start=1):
            s = (samsungTvId, samsungTv, samsungTvs.get(samsungTv)[0], 1, samsungTvs.get(samsungTv)[1])
            insertSamsungTv(connection, s)
        for lgTvId, lgTv in enumerate(lgTvs, start=1):
            l = (lgTvId, lgTv, lgTvs.get(lgTv)[0], 2, lgTvs.get(lgTv)[1])
            insertLgTv(connection, l)
        for xaiomiTvId, xiaomiTv in enumerate(xiaomiTvs, start=1):
            x = (xaiomiTvId, xiaomiTv, xiaomiTvs.get(xiaomiTv)[0], 3, xiaomiTvs.get(xiaomiTv)[1])
            insertXiaomiTv(connection, x)
        for sonyTvId, sonyTv in enumerate(sonyTvs, start=1):
            s = (sonyTvId, sonyTv, sonyTvs.get(sonyTv)[0], 4, sonyTvs.get(sonyTv)[1])
            insertSonyTv(connection, s)
        for philipsTvId, philipsTv in enumerate(philipsTvs, start=1):
            p = (philipsTvId, philipsTv, philipsTvs.get(philipsTv)[0], 5, philipsTvs.get(philipsTv)[1])
            insertPhilipsTv(connection, p)
        for toshibaTvId, toshibaTv in enumerate(toshibaTvs, start=1):
            t = (toshibaTvId, toshibaTv, toshibaTvs.get(toshibaTv)[0], 6, toshibaTvs.get(toshibaTv)[1])
            insertToshibaTv(connection, t)
    
    # СОЗДАНИЕ ТАБЛИЦ ДЛЯ МОДЕЛЕЙ НОУТБУКОВ
    with connection:
        createLaptopsBrands(connection)
        createLenovoLaptop(connection)
        createAsusLaptop(connection)
        createAcerLaptop(connection)
        createAppleLaptop(connection)
        createHpLaptop(connection)
        createDellLaptop(connection)
        for laptopBrandId, laptopBrand in enumerate(laptopBrandsAndAmount, start=1):
            l = (laptopBrandId, laptopBrand, laptopBrandsAndAmount.get(laptopBrand), 25)
            insertLaptopBrands(connection, l)
        for lenovoId, lenovoLaptop in enumerate(lenovoLaptops, start=1):
            l = (lenovoId, lenovoLaptop, lenovoLaptops.get(lenovoLaptop)[0], 1, lenovoLaptops.get(lenovoLaptop)[1])
            insertLenovoLaptop(connection, l)
        for asusId, asusLaptop in enumerate(asusLaptops, start=1):
            a = (asusId, asusLaptop, asusLaptops.get(asusLaptop)[0], 2, asusLaptops.get(asusLaptop)[1])
            insertAsusLaptop(connection, a)
        for acerId, acerLaptop in enumerate(acerLaptops, start=1):
            a = (acerId, acerLaptop, acerLaptops.get(acerLaptop)[0], 3, acerLaptops.get(acerLaptop)[1])
            insertAcerLaptop(connection, a)
        for macbookId, macbook in enumerate(macbooks, start=1):
            m = (macbookId, macbook, macbooks.get(macbook)[0], 4, macbooks.get(macbook)[1])
            insertAppleLaptop(connection, m)
        for hpId, hpLaptop in enumerate(hpLaptops, start=1):
            h = (hpId, hpLaptop, hpLaptops.get(hpLaptop)[0], 5, hpLaptops.get(hpLaptop)[1])
            insertHpLaptop(connection, h)
        for dellId, dellLaptop in enumerate(dellLaptops, start=1):
            d = (dellId, dellLaptop, dellLaptops.get(dellLaptop)[0], 6, dellLaptops.get(dellLaptop)[1])
            insertDellLaptop(connection, d)
    
    # СОЗДАНИЕ ТАБЛИЦ ДЛЯ ПЛАНШЕТОВ
    with connection:
        createTabletBrands(connection)
        createSamsungTablet(connection)
        createLenovoTablet(connection)
        createAppleTablet(connection)
        createAlcatelTablet(connection)
        createHuaweiTablet(connection)
        
    #-----------------------------------------------------------------------------------------------------------------------




if __name__ == '__main__':
    main()