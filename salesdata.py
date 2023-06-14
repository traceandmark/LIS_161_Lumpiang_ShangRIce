import sqlite3
from flask import g, session


db_path = "sales.db"



# This function conencts to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def connect(path):
    sql = sqlite3.connect(path)
    # Converting tuples to dictionaries
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, sqlite3):
        g.sqlite_db = connect()
    return  g.sqlite_db

def all():
    db= connect(db_path)
    cur = db.execute("SELECT * FROM LSRs")
    myresult = cur.fetchall()
    return myresult


# This function returns LSRs by flavor
def read_LSR_by_flavor(LSR_flavor):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM LSRs WHERE flavor = ?'
    value = LSR_flavor
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function returns LSRs by flavor
def read_LSR_by_rate(LSR_rate):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM LSRs WHERE rate = ?'
    value = LSR_rate
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function returns LSRs by flavor
def read_LSR_by_date(LSR_date):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM LSRs WHERE date = ?'
    value = LSR_date
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function returns LSRs by flavor
def read_LSR_by_customer(LSR_customer):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM LSRs WHERE customer = ?'
    value = LSR_customer
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function retrieves 1 LSR Expenses Data by LSR_id
def read_LSR_by_LSR_id(LSR_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM LSRs WHERE id = ?'
    value = LSR_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

# This function inserts 1 LSR Expenses data
def insert_LSR(LSR_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO LSRs (flavor, customer, contact, date, quantity, price, rate, feedback, url) VALUES (?, ?, ?, ?,?,?,?,?,?)'
    values = (LSR_data['flavor'], LSR_data['customer'],
              LSR_data['contact'], LSR_data['date'],
              LSR_data['quantity'], LSR_data['price'],
              LSR_data['rate'], LSR_data['feedback'], LSR_data['url'] )
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function updates a record
def update_LSR(LSR_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE LSRs SET flavor=?, customer=?, contact=?, date=?, quantity=?, price=?, rate=?, feedback=?, url=? WHERE id=?"
    values = (LSR_data['flavor'], LSR_data['customer'],
              LSR_data['contact'], LSR_data['date'],
              LSR_data['quantity'], LSR_data['price'],
              LSR_data['rate'], LSR_data['feedback'], 
              LSR_data['url'], LSR_data['LSR_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_LSR_id(LSR_id):
    d = LSR_id
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM LSRs WHERE id = ?"
    value = d
    cur.execute(query, (d,))
    conn.commit()
    conn.close()
