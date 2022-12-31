from flask import Flask, jsonify, request, render_template, make_response, url_for, redirect
from flask_mysqldb import MySQL
from flask_cors import CORS
import ast


app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DefinetlyNotAmazon'
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
    query_string = "SELECT * FROM customer WHERE email = %s AND password = %s;"
    cursor.execute(query_string, (email, password))
    validation = cursor.fetchall()
    cursor.close()
    # Should check if validation has an element, if it does, allow login
    return jsonify(validation)


@app.route('/home', methods=['GET'])
def home():
    cursor = mysql.connection.cursor()
    query_string = "SELECT * FROM product ORDER BY date_added DESC LIMIT 85, 5;"
    cursor.execute(query_string),
    query = cursor.fetchall()
    data = load_data(cursor, query)
    cursor.close()

    return data
    

@app.route('/product/<id>', methods=['GET','POST'])
def product(id):
    cursor = mysql.connection.cursor()
    data = dictify(request)
    query = 'SELECT * FROM product WHERE product_id=%s;'%(data['product_id'])
    cursor.execute(query)
    result = cursor.fetchall()

    return url_for(result)


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