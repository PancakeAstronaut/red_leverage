import sqlite3


def arb():
    print("Not supposed to see this")


def credentials_validator(username, password):
    dbconnection = sqlite3.connect('login.db')
    sqlite_cursor = dbconnection.cursor()
    sqlite_cursor.execute("SELECT UserName, UserPassword FROM LoginInfo WHERE UserName = (?) AND UserPassword = (?)", (username, password, ))
    resultList = sqlite_cursor.fetchall()
    if len(resultList) <= 0:
        return [0, 0]
    else:
        db_stored_passwd = resultList[0][1]
        db_stored_uname = resultList[0][0]
        return_list = [db_stored_uname, db_stored_passwd]
        return return_list


if __name__ == '__main__':
    arb()
