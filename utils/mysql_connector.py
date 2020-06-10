import mysql.connector
import logging

logging.basicConfig(level=logging.DEBUG)


def connect(host, user, password, database):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except Exception as e:
        logging.error('failed to connect db {}'.format(e))
    finally:
        return conn


def select(query):
    conn = connect('localhost', 'root', 'danielroot', 'stx_analyzer')
    results = None
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        print(columns)
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        cursor.close()
    except Exception as e:
        logging.error('failed to query db {}'.format(e))
    finally:
        conn.close()
        return results


def insert(query, args):
    conn = connect('localhost', 'root', 'danielroot', 'stx_analyzer')
    try:
        cursor = conn.cursor()
        cursor.executemany(query, args)
        conn.commit()
        logging.debug("{} record inserted.".format(cursor.rowcount))
    except Exception as e:
        print("failed to insert data to db {}".format(e))
    finally:
        conn.close()
