import sqlite3
from flask import g

db_path = "inventory.db"

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

def inv_all():
    db= connect(db_path)
    cur = db.execute("SELECT * FROM INVs")
    myresult = cur.fetchall()
    return myresult

# This function returns INVs by item
def read_LSR_by_item(LSR_type):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM INVs WHERE type = ?'
    value = LSR_type
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

# This function retrieves 1 LSR Expenses invdata by LSR_inv_id
def read_LSR_by_LSR_inv_id(LSR_inv_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM INVs WHERE invid = ?'
    value = LSR_inv_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

# This function inserts 1 LSR Inventory Data
def insert_invLSR(LSR_invdata):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO INVs (type, item, description, stock, unit, amount, total) VALUES (?, ?, ?, ?, ?, ?, ?)'
    values = ( (LSR_invdata['type'], LSR_invdata['item'], LSR_invdata['description'],
              LSR_invdata['stock'], LSR_invdata['unit'],
              LSR_invdata['amount'], LSR_invdata['total']))
    cur.execute(query,values)
    conn.commit()
    conn.close()

# This function update a record
def inv_update_LSR(LSR_invdata):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE INVs SET type =?, item=?, description=?, stock=?, unit=?, amount=?,  total=? WHERE invid=?"
    values = (LSR_invdata['type'], LSR_invdata['item'], 
              LSR_invdata['description'],LSR_invdata['stock'], 
              LSR_invdata['unit'], LSR_invdata['amount'], 
              LSR_invdata['total'], LSR_invdata['LSR_inv_id'])
    cur.execute(query, values)
    conn.commit()
    results = cur.execute(query,(values)).fetchall()
    conn.close()
    return results

def delete_INV_id(LSR_inv_id):
    d = LSR_inv_id
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM INVs WHERE invid = ?"
    value = d
    cur.execute(query, (d,))
    conn.commit()
    conn.close()

