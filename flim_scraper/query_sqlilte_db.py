import sqlite3


def get_all_tables(conn):
    cur = conn.cursor()
    cur.execute("select name from sqlite_master where type='table'")
    print(cur.fetchall())


def get_all_from_table(conn, table):
    print(f"Getting all rows from table {table}...")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    # print column names
    names = [description[0] for description in cur.description]
    print("column names: ", names)
    # print all rows
    if len(rows) != 0:
        for row in rows:
            print(row)
    else:
        print('No rows in table movie.')
    # columns type
    print('\nColumn types:')
    cur.execute(f'pragma table_info({table})')
    for col in cur.fetchall():
        name = col[1]
        type = col[2]
        print(f"\t{name} - {type}")


if __name__ == '__main__':
    db = "./app.db"
    table = 'movies'

    conn = sqlite3.connect(db)
    with conn:
        get_all_tables(conn)
        get_all_from_table(conn, table)

