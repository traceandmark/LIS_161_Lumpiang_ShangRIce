from flask import Flask, render_template, request, redirect, url_for
from salesdata import *
from inventorydata import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/LumpiangShangRice/menu')
def menu():
    return render_template("menu.html")

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# ---------------------------------------- Inventory ------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

@app.route('/LumpiangShangRice/form/inventory')
def inventory_form():
    return render_template("inventoryform.html")

@app.route('/LumpiangShangRice/inventory')
def inventory_database():
    data = inv_all()
    return render_template("inventorydata.html", data=data)

@app.route('/Lumpiang/<int:LSR_inv_id>')
def INV_LSR(LSR_inv_id):
    INV = read_LSR_by_LSR_inv_id(LSR_inv_id)
    return render_template("inventory.html", INV=INV)

@app.route('/inv_processed', methods=['post'])
def inv_processing():
    LSR_invdata = {
        "type": request.form['LSR_type'],
        "item": request.form['LSR_item'],
        "description": request.form['LSR_description'],
        "stock": request.form['LSR_stock'],
        "unit": request.form['LSR_unit'],
        "amount": request.form['LSR_amount'],
        "total": request.form['LSR_total']

    }
    insert_invLSR(LSR_invdata)
    return redirect(url_for('item',inv_type=request.form['LSR_type']))

@app.route('/LumpiangShangRice/inventory/<inv_type>')
def item (inv_type):
    item = inv_type
    INVs = read_LSR_by_item(inv_type)
    return render_template("items.html", item = item, INVs=INVs)

@app.route('/imodify/<int:LSR_inv_id>', methods=['post'])
def inv_modify(LSR_inv_id):
    INV = read_LSR_by_LSR_inv_id(LSR_inv_id)
    if request.form["action"] == "View":
        # retrieve record using id
        LSR_inv_id = request.form["LSR_inv_id"] 
        return redirect(url_for('INV_LSR',LSR_inv_id=LSR_inv_id))
    # 1. identify whether user clicked edit or delete
       # if edit, then do this:
    elif request.form["action"] == "Edit":
        # retrieve record using id
        LSR_inv_id = request.form["LSR_inv_id"] 
        # update record with new data
        return render_template('inventoryupdate.html', INV=INV)
    # if delete, then do this
    elif request.form["action"] == "Delete":
        # retrieve record using id
        # delete the record
        delete_INV_id(LSR_inv_id)
        # redirect user to LSR list by LSR type
        return redirect(url_for('inventory_database'))
    
@app.route('/inv_update', methods=['post'])
def inv_update():
    LSR_invdata = {
        "LSR_inv_id" : request.form["LSR_inv_id"],
        "type": request.form['LSR_type'],
        "item": request.form['LSR_item'],
        "description": request.form['LSR_description'],
        "stock": request.form['LSR_stock'],
        "unit": request.form['LSR_unit'],
        "amount": request.form['LSR_amount'],
        "total": request.form['LSR_total']
    }
    inv_update_LSR(LSR_invdata)
    return redirect(url_for('INV_LSR', LSR_inv_id = request.form['LSR_inv_id']))

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# ----------------------------------------- Sales--------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

@app.route('/LumpiangShangRice/form/sales')
def sales_form():
    return render_template("salesform.html")


@app.route('/LumpiangShangRice/sales')
def sales_database():
    data = all()
    return render_template("salesdata.html", data=data)


@app.route('/LumpiangShangRice/<int:LSR_id>')
def LSR(LSR_id):
    LSR = read_LSR_by_LSR_id(LSR_id)
    return render_template("sales.html", LSR=LSR)

@app.route('/processed', methods=['post'])
def processing():
    LSR_data = {
        "flavor": request.form['LSR_flavor'],
        "customer": request.form['LSR_customer'],
        "contact": request.form['LSR_contact'],
        "date": request.form['LSR_date'],
        "quantity": request.form['LSR_quantity'],
        "price": request.form['LSR_price'],
        "rate": request.form['LSR_rate'],
        "feedback": request.form['LSR_feedback'],
        "url": request.form['LSR_url']
    }
    insert_LSR(LSR_data)
    return redirect(url_for('flavor',shangrice_flavor=request.form['LSR_flavor']))  
def rate_processing():
    LSR_data = {
        "flavor": request.form['LSR_flavor'],
        "customer": request.form['LSR_customer'],
        "contact": request.form['LSR_contact'],
        "date": request.form['LSR_date'],
        "quantity": request.form['LSR_quantity'],
        "price": request.form['LSR_price'],
        "rate": request.form['LSR_rate'],
        "feedback": request.form['LSR_feedback'],
        "url": request.form['LSR_url']
    }
    insert_LSR(LSR_data)
    return redirect(url_for('rate_item',rate=request.form['LSR_rate']))
def customer_processing():
    LSR_data = {
        "flavor": request.form['LSR_flavor'],
        "customer": request.form['LSR_customer'],
        "contact": request.form['LSR_contact'],
        "date": request.form['LSR_date'],
        "quantity": request.form['LSR_quantity'],
        "price": request.form['LSR_price'],
        "rate": request.form['LSR_rate'],
        "feedback": request.form['LSR_feedback'],
        "url": request.form['LSR_url']
    }
    insert_LSR(LSR_data)
    return redirect(url_for('customer_item',customer=request.form['LSR_customer']))
def date_processing():
    LSR_data = {
        "flavor": request.form['LSR_flavor'],
        "customer": request.form['LSR_customer'],
        "contact": request.form['LSR_contact'],
        "date": request.form['LSR_date'],
        "quantity": request.form['LSR_quantity'],
        "price": request.form['LSR_price'],
        "rate": request.form['LSR_rate'],
        "feedback": request.form['LSR_feedback'],
        "url": request.form['LSR_url']
    }
    insert_LSR(LSR_data)
    return redirect(url_for('date_item',date=request.form['LSR_date']))


@app.route('/LumpiangShangRice/sales/<shangrice_flavor>')
def flavor (shangrice_flavor):
    flavor = shangrice_flavor
    LSRs = read_LSR_by_flavor(flavor)
    return render_template("products.html", flavor = flavor, LSRs=LSRs)

@app.route('/LumpiangShangRice/sales/rate/<rate>')
def rate_item (rate):
    rate = rate
    LSRs = read_LSR_by_rate(rate)
    return render_template("rate.html", rate = rate, LSRs=LSRs)

@app.route('/LumpiangShangRice/sales/date/<date>')
def date_item (date):
    date = date
    data = all()
    LSRs = read_LSR_by_date(date)
    return render_template("date.html", date = date, LSRs=LSRs, data=data)

@app.route('/LumpiangShangRice/sales/customer/<customer>')
def customer_item (customer):
    customer = customer
    data = all()
    LSRs = read_LSR_by_customer(customer)
    return render_template("customer.html", customer = customer, LSRs=LSRs, data=data)

@app.route('/LumpiangShangRice/<type>')
def sales_type(type):
    initial = ""
    if type == "rate":
        data = all()
        return render_template("ratepage.html", data=data)
    elif type == "date":
        data = all()
        return render_template("datepage.html", data=data)
    elif type == "customer":
        data = all()

        return render_template("customerpage.html", data=data)
    if type == "flavor":
        data = all()
        return render_template("flavor.html", data=data)



@app.route('/modify/<int:LSR_id>', methods=['post'])
def modify(LSR_id):
    LSR =  read_LSR_by_LSR_id(LSR_id)
    if request.form["action"] == "View":
        # retrieve record using id
        return redirect(url_for('LSR',LSR_id=LSR_id))
    # 1. identify whether user clicked edit or delete
       # if edit, then do this:
    elif request.form["action"] == "Edit":
        # retrieve record using id
        LSR_id = request.form["LSR_id"] 
        # update record with new data
        return render_template('salesupdate.html', LSR=LSR)
    # if delete, then do this
    elif request.form["action"] == "Delete":
        # delete the record
        delete_LSR_id(LSR_id)
        # redirect user to LSR list by LSR type
        return redirect(url_for('sales_database'))

@app.route('/update', methods=['get', 'post'])
def update():
    LSR_data = {
        "LSR_id" : request.form["LSR_id"],
        "flavor": request.form['LSR_flavor'],
        "customer": request.form['LSR_customer'],
        "contact": request.form['LSR_contact'],
        "date": request.form['LSR_date'],
        "quantity": request.form['LSR_quantity'],
        "price": request.form['LSR_price'],
        "rate": request.form['LSR_rate'],
        "feedback": request.form['LSR_feedback'],
        "url": request.form['LSR_url']
    }
    update_LSR(LSR_data)
    return redirect(url_for('LSR', LSR_id = request.form['LSR_id']))

if __name__ == "__main__":
    app.run(debug=True)

