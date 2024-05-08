from flask import g, request, jsonify
import sqlite3

from dbapipackage import db
from dbapipackage import app

@app.route("/", methods=['GET'])
def index():
    return '<h1>Hello, World!</h1>'

@app.route("/users")
def viewusers():
    db1 = db.get_db()
    cursor = db1.execute('select id, name, age from users')
    results = cursor.fetchall()
    #return "<h1> Welcome to Users </h1>"
    return f"<h1>The Id is {results[0]['id']}.<br> The Name is {results[0]['name']}. <br> The age is {results[0]['age']}. </h1>"


#CREATE
@app.route('/users', methods=['POST'])
def create_user():
    db1 = db.get_db()
    name = request.json['name']
    age = request.json['age']
    db1.execute('INSERT INTO users (name, age) VALUES (?, ?)', [name, age])
    db1.commit()
    return jsonify({'message': 'User created successfully!'})


#READ
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db1 = db.get_db()
    cursor = db1.execute('SELECT * FROM users WHERE id = ?', [user_id])
    result = cursor.fetchone()
    if not result:
        return jsonify({'error': 'User not found'})
    return f"<h1>The Id is {result['id']}.<br> The Name is {result['name']}. <br> The age is {result['age']}. </h1>"
    #return jsonify({'id': result['id'], 'name': result['name'], 'age': result['age']})


#UPDATE
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db1 = db.get_db()
    name = request.json['name']
    age = request.json['age']
    db1.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', [name, age, user_id])
    db1.commit()
    return jsonify({'message': 'User updated successfully!'})


#DELETE
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db1 = db.get_db()
    db1.execute('DELETE FROM users WHERE id = ?', [user_id])
    db1.commit()
    return jsonify({'message': 'User deleted successfully!'})