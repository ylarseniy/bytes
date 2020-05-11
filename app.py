from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/<string:data>', methods=['post'])
def main(data):
    n = int(data, 2)
    dec = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(dec)
    return {}


if __name__ == '__main__':
    app.run()
