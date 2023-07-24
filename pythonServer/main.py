from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)

# Sample data to store products (you can replace this with a database in a real application)
products = []


@app.route('/products', methods=['GET'])
def add_product():
    # Create a new product
    new_product = {
        'name': f'product #{len(products) + 10}',
        'price': f'{100 + len(products) + 10}'
    }
    products.append(new_product)

    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
