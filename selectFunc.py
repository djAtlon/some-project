import os
import sqlite3
from sqlite3 import Error

def selectCategories(connection):
    sql_select_from_categories = """SELECT name FROM categories;"""
    rows = []
    try:
        cursor = connection.cursor()
        cursor.execute(sql_select_from_categories)
        rows = cursor.fetchall()
    except Error as error:
        print(error)
    finally:
        return rows


def main():
    dbFile = r'C:\stuff\uni_course 4\pythonStuff\some-project\database.db'
    if os.path.exists(dbFile):
        connection = sqlite3.connect(dbFile)
        with connection:
            showCategories = selectCategories(connection)
            for showCategory in showCategories:
                print(list(showCategory)[0])



if __name__ == '__main__':
    main()