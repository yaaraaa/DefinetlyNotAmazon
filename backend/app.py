from flask import Flask, jsonify, request, render_template, make_response, url_for, redirect
from flask_mysqldb import MySQL
from flask_cors import CORS
import ast
import re


app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root123*'
app.config['MYSQL_DB'] = 'onlShop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)


@app.route('/register', methods = ['GET', 'POST'])
def Register():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        data = request.get_data().decode("UTF-8")
        user = ast.literal_eval(data)

        cursor.execute('''INSERT INTO customer (email, 
                                                password, 
                                                balance, 
                                                username, 
                                                Bdate, 
                                                Fname, 
                                                Lname, 
                                                floor, 
                                                street, 
                                                area, 
                                                city, 
                                                country)
            VALUES ('%s', '%s', 0.0, '%s', '%s', '%s', '%s', NULL, NULL, NULL, NULL, NULL);'''%
                                               (user['email'], 
                                                user['password'], 
                                                user['firstname']+' '+user['lastname'], 
                                                user['dateOfBirth'], 
                                                user['firstname'], 
                                                user['lastname']))
        mysql.connection.commit()
        cursor.close()
    else:
        return load_data('customer')
        # return 'User successfully registered'

    # else:
    #     cursor.execute('SELECT * FROM customer;')
    #     data = cursor.fetchall()
    #     cursor.close()
    #     return jsonify(data)
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Should be checked in POST
    data = dictify(request)
    email, password = data['email'], data['password']

    cursor = mysql.connection.cursor()
    query_statement = "SELECT * FROM customer WHERE email = %s AND password = %s;"
    cursor.execute(query_statement, (email, password))
    validation = cursor.fetchall()
    cursor.close()
    
    # Should check if validation has an element, if it does, allow login
    return jsonify(validation)


@app.route('/home', methods=['GET'])
def home():
    cursor = mysql.connection.cursor()
    query_statement = "SELECT * FROM product ORDER BY date_added DESC LIMIT 85, 5;"
    cursor.execute(query_statement),
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