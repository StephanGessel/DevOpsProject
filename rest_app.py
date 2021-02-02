from db_connector import *
from flask import Flask, request

app = Flask(__name__)

@app.route('/users/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])

def user(id):
    if request.method == 'POST':
        try:

            name = request.json.get('name')
            print('exe')
            set_data(id, name)
            return {'status': 'ok', 'user added': name}, 201  # status code
        except:
            return {'status': 'error', 'reason': f"ID {id} already exists"}, 500  # status code

    elif request.method == 'GET':
        try:
            name = get_data(id)
            return {'status': 'ok', 'name': name}, 200
        except:
            return {'status': 'error', 'reason': "No such id"}, 500  # status code

    elif request.method == 'PUT':
        try:

            name = request.json.get('name')
            update(id, name)
            return {'status': 'ok', 'user_updated': name}, 200  # status code
        except:
            return {"status": "error", "reason": "No such id"}, 500

    elif request.method == 'DELETE':
        try:
            remove(id)
            return {'status': 'ok', 'user_deleted': id}, 200  # status code
        except:
            return {'status': 'error', 'reason': "Mo such id"}, 500

app.run(host='127.0.0.1', debug=True, port=5000)