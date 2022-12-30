from flask import Flask, jsonify, request, render_template
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
    cursor = mysql.connection.cursor()
    if request.method == "POST":
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
    return load_data('product')
    

def dictify(request):
    'Converts request byte object to dictionary'
    return ast.literal_eval(request.get_data().decode('UTF-8'))


def load_data(table):
    cursor = mysql.connection.cursor()
    query_string = "SELECT * FROM %s"% (table)
    cursor.execute(query_string)
    query = cursor.fetchall()
    cursor.close()

    fields = []
    for items in cursor.description:
        fields.append(items[0])

    instance, all_instances = {}, []
    for row in query:
        instance.update(zip(fields, row))
        all_instances.append(instance)
    return jsonify(all_instances)


if __name__ == "__main__":
    app.run(debug=True)