import mysql.connector
import logging


class MySqlConnector:
    host = 'localhost'
    user = 'root'
    password = 'danielroot'
    database = 'stx_analyzer'
    conn = None

    @classmethod
    def connect(cls):
        try:
            cls.conn = mysql.connector.connect(
                host=cls.host,
                user=cls.user,
                password=cls.password,
                database=cls.database
            )
        except Exception as e:
            logging.error('failed to connect db : {}'.format(e))

    def select(self, query):
        results = None
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            cursor.close()
        except Exception as e:
            logging.error('failed to query db {}'.format(e))
        finally:
            try:
                self.conn.close()
            except Exception as e:
                logging.error('failed to close db connection : {}'.format(e))
        return results

    def insert(self, query, records):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.executemany(query, records)
            self.conn.commit()
        except Exception as e:
            print("failed to insert records to db {}".format(e))
        finally:
            try:
                self.conn.close()
            except Exception as e:
                logging.error('failed to close db connection : {}'.format(e))

    def update(self, query, columns_list):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.executemany(query, columns_list)
            self.conn.commit()
        except Exception as e:
            print("failed to update columns list in db {}".format(e))
        finally:
            try:
                self.conn.close()
            except Exception as e:
                logging.error('failed to close db connection : {}'.format(e))

    def delete(self, query, args):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.executemany(query, args)
            self.conn.commit()
        except Exception as e:
            print("failed to delete records in db {}".format(e))
        finally:
            try:
                self.conn.close()
            except Exception as e:
                logging.error('failed to close db connection : {}'.format(e))
