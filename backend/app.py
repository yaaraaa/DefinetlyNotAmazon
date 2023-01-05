from flask import Flask, jsonify, request, render_template, make_response, url_for, redirect
from flask_mysqldb import MySQL
from flask_cors import CORS
import hashlib
import ast
import re
from datetime import date


app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DefinetlyNotAmazon'
app.config['MYSQL_DB'] = 'onlShop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)


@app.route('/update', methods=['POST'])
def updateProduct():
    cursor = mysql.connection.cursor()
    productData = dictify(request)
    today = date.today()

    query_statement = '''UPDATE Product SET
        date_updated = '%s',
        name = '%s',
        price = %s,
        image = '%s',
        brand = '%s',
        model = '%s',
        quantity = %s 
        WHERE product_id = %s'''%(
            today,
            productData['productName'],
            productData['price'],
            productData['image'],
            productData['brand'],
            productData['model'],
            productData['quantity'],
            productData['productID'])
    
    cursor.execute(query_statement)
    mysql.connection.commit()
    cursor.close()
    return "success"


@app.route('/delete', methods=['POST'])
def deleteProduct():
    cursor = mysql.connection.cursor()
    productData = dictify(request)

    query_statement = "SELECT * FROM Product WHERE product_id=%s;"%(productData['productID'])
    
    cursor.execute(query_statement)
    result = cursor.fetchall()
    
    status = dict()
    status['idExists'] = '1' if len(result) != 0 else ''

    query_statement = '''DELETE FROM Product WHERE product_id=%s'''%(productData['productID'])

    cursor.execute(query_statement)
    mysql.connection.commit()

    cursor.close()
    return status


@app.route('/add', methods=['POST'])
def addProduct():
    cursor = mysql.connection.cursor()
    productData = dictify(request)

    today = date.today()

    query_statement = '''INSERT INTO product (
        date_added,
        name,
        price,
        image,
        brand,
        model,
        quantity,
        discount_amount) VALUES ('%s','%s',%s,'%s','%s','%s',%s,%s)
        '''%(
            today,
            productData['productName'],
            productData['price'],
            productData['image'],
            productData['brand'],
            productData['model'],
            productData['quantity'],
            productData['discount']
        )

    cursor.execute(query_statement)
    mysql.connection.commit()

    cursor.close()
    return "success"


@app.route('/home', methods=['GET'])
def home():
    cursor = mysql.connection.cursor()
    query_statement = "SELECT * FROM product ORDER BY date_added DESC;"
    cursor.execute(query_statement)
    result = cursor.fetchall()
    data = load_data(cursor, result)
    cursor.close()

    return data
    

@app.route('/product/<id>', methods=['GET'])
def product(id):
    cursor = mysql.connection.cursor()
    query_statement = 'SELECT * FROM product WHERE product_id=%s;'%(id)
    cursor.execute(query_statement)
    result = cursor.fetchall()
    data = load_data(cursor, result)
    return data


@app.route('/category/<category>')
def category(category):
    '''
    accessories, tablets, mobiles, speakers, tv, parts, adapters, storage, 
    '''
    cursor = mysql.connection.cursor()
    query_statement = 'SELECT * FROM product WHERE product_id=%s;'%(id)
    cursor.execute(query_statement)
    result = cursor.fetchall()
    data = load_data(cursor, result)
    return data


@app.route('/search/<query>', methods=['POST'])
def search(query):
    cursor = mysql.connection.cursor()
    query_statement = 'SELECT * FROM product;'
    cursor.execute(query_statement)
    result = cursor.fetchall()
    data = load_data(cursor, result)

    response = []
    for row in dictify(data):
        if re.findall(query, row['name'], flags=re.IGNORECASE):
            response.append(row)

    return response


@app.route('/register', methods = ['POST'])
def Register():
    cursor = mysql.connection.cursor()
    user = dictify(request)
    
    # Hashing the password
    salt = "5gz"
    dataBase_password = user['password']+salt
    hashed = hashlib.md5(dataBase_password.encode())

    cursor.execute('''INSERT INTO customer (email, 
                                            password, 
                                            balance, 
                                            Bdate, 
                                            Fname, 
                                            Lname, 
                                            floor, 
                                            street, 
                                            area, 
                                            city, 
                                            country)
        VALUES ('%s', '%s', 0.0, '%s', '%s', '%s', NULL, NULL, NULL, NULL, NULL);'''%
                                            (user['email'], 
                                            hashed.hexdigest(),  
                                            user['birthdate'], 
                                            user['firstname'], 
                                            user['lastname']))
    mysql.connection.commit()
    cursor.close()

    return "Success"
    


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Should be checked in POST
    data = dictify(request)
    email = data['email']
    password = data['password']

    # Hashing the password
    # salt = "5gz"
    # dataBase_password = data['password']+salt
    # hashed = hashlib.md5(dataBase_password.encode())

    cursor = mysql.connection.cursor()
    query_statement = f"SELECT * FROM customer WHERE email = '{email}' AND password = '{password}';"
    
    cursor.execute(query_statement)
    result = cursor.fetchall()
    
    status = dict()
    status['status'] = '1' if len(result) != 0 else ''

    data = load_data(cursor, result)
    cursor.close()
    
    # Should check if validation has an element, if it does, allow login
    return status



def dictify(request):
    'Converts request byte object to dictionary'
    return ast.literal_eval(request.get_data().decode('UTF-8'))


def load_data(cursor, query):
    # cursor = mysql.connection.cursor()
    # query_string = "SELECT * FROM %s"% (table)
    # cursor.execute(query_string)
    # query = cursor.fetchall()
    # cursor.close()
    
    fields = []
    for items in cursor.description:
        fields.append(items[0])

    all_instances = []
    for row in query:
        all_instances.append(dict(zip(fields, row)))

    return make_response(all_instances)


if __name__ == "__main__":
    app.run(debug=True)