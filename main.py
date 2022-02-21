from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)


@app.route('/userLogin', methods=['POST'])
def userLogin():
    user_name = request.get_json()  # json 데이터를 받아옴, type -> dict
    print(type(user_name["userName"]))
    name = json.dumps(user_name)    # dict to str
    print(type(name))
    return jsonify(user_name)  # 받아온 데이터를 다시 전송


@app.route('/sayHello', methods=['POST'])
def sayHello():
    # name = request.get_json()
    name = request.get_data()
    print(str(name))
    return str(name)


@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'corgi.jpg'
    else:
       filename = 'error.jpg'
    return send_file(filename, mimetype='image/jpg')


@app.route('/environments/<language>', methods=['GET'])
def environments(language):
    return jsonify({"language": language})


if __name__ == "__main__":
    app.run()
