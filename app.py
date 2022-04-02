from flask import Flask, jsonify
from flask.helpers import send_from_directory
import json
from .parser import GreenvilleTaxSalesParser
from flask_cors import CORS, cross_origin
app = Flask(__name__, static_folder='greenville-sc-tax-sales/build',
            static_url_path='')
CORS(app)


@app.route("/api/", methods=["GET"])
@cross_origin()
def index():
    parser = GreenvilleTaxSalesParser()
    tax_sales = parser.get_tax_sales_list()
    tax_sales = parser.sort_tax_sales_by_amount_due(tax_sales)
    tax_sales = {
        'taxSales': tax_sales
    }
    return jsonify(tax_sales)


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()
