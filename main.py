from flask import Flask, request, jsonify, send_file
import json
import os
from PIL import Image
from base64 import encodebytes
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/userLogin', methods=['POST'])
def userLogin():
    user_name = request.get_json()  # json 데이터를 받아옴, type -> dict
    print(type(user_name["userName"]))
    name = json.dumps(user_name)  # dict to str
    print(type(name))
    return jsonify(user_name)  # 받아온 데이터를 다시 전송


@app.route('/sayHello', methods=['POST'])
def sayHello():
    # name = request.get_json()
    name = request.get_data()
    print(str(name))
    return str(name)


@app.route('/get_image')
def get_image1():
    if request.args.get('type') == '1':
        filename = 'corgi.jpg'
    else:
        filename = 'error.jpg'
    return send_file(filename, mimetype='image/jpg')


@app.route('/environments/<language>', methods=['GET'])
def environments(language):
    return jsonify({"language": language})


def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r')
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG')
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')
    return encoded_img


@app.route('/images/clothes/<category>/<image_name>', methods=['GET'])
def get_image(category, image_name):
    image_path = './clothes/' + category + '/' + image_name
    return send_file(image_path, mimetype='image/png')


@app.route('/settings/init', methods=['GET'])
def initial_settings():
    categories = ['OUTER', 'DRESS', 'PANTS', 'SKIRT', 'TOP']

    json_data = {
        'clothes': []
    }
    path_dir = '/clothes'
    for category in categories:
        detail_path_dir = '.' + path_dir + '/' + category
        file_list = os.listdir(detail_path_dir)

        for element_name in file_list:
            data = {'category': category}
            img_name = '/images' + path_dir + '/' + category + '/' + element_name
            # data['result'] = get_response_image(img_name)
            data['image'] = img_name
            json_data['clothes'].append(data)

    return jsonify(json_data)


@app.route('/')
def home():
    return "my home"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
