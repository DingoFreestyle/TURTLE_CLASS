import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

# 포스트맨.exe를 이용해서 다양한 신호들을 보내고 답변을 받을 수 있음
# 프론트엔드 제작 전에 사전 백엔드 작업을 할 수 있도록 해서 작업에 용이

# 잘 되는지 확인하는 파트


@app.route("/")
def home():
    return jsonify({'message': 'success'})


# 회원가입 파트, 정보를 주고 받아야 하니 POST
@app.route("/signup", methods=["POST"])
def sign_up():
    print(request)
    print(request.form)
    print(request.data)
    data = json.loads(request.data)
    print(data)
    print(data.get('id'))
    print(data["password"])
    # print(request.form['id'])으로 해놓고 id 값이 없거나 이상한 경우 에러를 유발
    print(request.form.get('id'))
    # print(request.form.get('id'))으로 해놓고 id 값이 없거나 이상한 경우 NONE으로 끝남
    # 안정성을 위해 get으로 들고 오는 것을 권장

    # form 대신 data를 요청할 수도 있는데, json으로 보내도록 세팅을 하여야 함
    # data = json.loads(request.data)

    return jsonify({'message': 'success123'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
