import pymysql

class LocalSql:

    def __init__(self, database):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='P@ssw0rd',
            port=3306,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_databases(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SHOW DATABASES;')
            result = cursor.fetchall()

        return result

    def show_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute('SHOW TABLES;')
            result = cursor.fetchall()

        return result

    def sql_query(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result


if __name__ == '__main__':
    # databases = LocalSql('my_ship').get_databases()

    my_ship_tables = LocalSql('my_ship').show_tables()
    my_titanic_table = LocalSql('my_titanic').show_tables()
    print(f'my_ship: {my_ship_tables}')
    print(f'my_titanic: {my_titanic_table}')

    # print(databases)

    # sql = 'SELECT * FROM full_passengers;'
    # result = LocalSql().sql_query(sql)
    
    # print(result[:5])