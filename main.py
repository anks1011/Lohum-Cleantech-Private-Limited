from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/price', methods=['GET'])
def get_price():
    try:
        url = 'https://www.metal.com/Lithium-ion-Battery/202303240001'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('span', {'class': 'strong___1JlBD priceDown___2TbRQ'}).text
        return jsonify({'price': price})
    except:
        return jsonify({'error': 'Could not retrieve price.'}), 500

if __name__ == '__main__':
    app.run()
