from flask import Flask, jsonify, request, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# from io import BytesIO
# from PIL import Image
import ast


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:"DefinetlyNotAmazon"@localhost/onlShop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('date_added', 'price', 'image', 'brand', 'model', 'quantity', 'name', 'discount_amount', 'date_updated')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DefinetlyNotAmazon'
app.config['MYSQL_DB'] = 'onlShop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)

@app.route('/register', methods = ['GET', 'POST'])
def Register():
    pass
    # cursor = mysql.connection.cursor()
    # if request.method == "POST":
    #     data = request.get_data().decode("UTF-8")
    #     user = ast.literal_eval(data)

    #     cursor.execute('''INSERT INTO customer (email, 
    #                                             password, 
    #                                             balance, 
    #                                             username, 
    #                                             Bdate, 
    #                                             Fname, 
    #                                             Lname, 
    #                                             floor, 
    #                                             street, 
    #                                             area, 
    #                                             city, 
    #                                             country)
    #         VALUES ('%s', '%s', 0.0, '%s', '%s', '%s', '%s', NULL, NULL, NULL, NULL, NULL);'''%
    #                                            (user['email'], 
    #                                             user['password'], 
    #                                             user['firstname']+' '+user['lastname'], 
    #                                             user['dateOfBirth'], 
    #                                             user['firstname'], 
    #                                             user['lastname']))

    #     mysql.connection.commit()
    #     cursor.close()

    #     return 'User successfully registered'

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
    query_string = "SELECT * FROM product;"
    cursor.execute(query_string)
    all_products = cursor.fetchall()
    results = products_schema.dump(all_products)
    cursor.close()
    print(jsonify(results))
    return jsonify(results)
    # return jsonify({image:"https://images-na.ssl-images-amazon.com/images/I/71oVh2UO8xL._SL1500_.jpg,http://pisces.bbystatic.com/image2/BestBuy_US/images/products/5689/5689019_sa.jpg,https://images-na.ssl-images-amazon.com/images/I/81EzIaCamJL._SL1500_.jpg,https://images-na.ssl-images-amazon.com/images/I/71X2tAW39aL._SL1500_.jpg,https://images-na.ssl-images-amazon.com/images/I/71c8xybNthL._SL1500_.jpg,http://static.bhphoto.com/images/smallimages/1368452917000_911749.jpg,http://static.bhphoto.com/images/images500x500/sanus_vlf410_b1_vlf410_super_slim_full_motion_1368452917000_911749.jpg,http://static.bhphoto.com/images/multiple_images/thumbnails/1368452838000_IMG_316474.jpg"})


def dictify(request):
    'Converts request byte object to dictionary'
    return ast.literal_eval(request.get_data().decode('UTF-8'))


if __name__ == "__main__":
    app.run(debug=True)