from flask import Blueprint, render_template, jsonify
from .db import get_db

bp = Blueprint('mainsite', __name__, url_prefix='/')

@bp.route('/')
def hello():
    db = get_db()
    result = db.execute('SELECT * FROM todoitem').fetchall()
    data = []
    for result_row in result:
       data.append(list(result_row))
    return jsonify(data)

@bp.route('/sample', methods=['POST'])
def sample():
    db = get_db()
    db.execute('INSERT INTO todoitem (title, todotype, todotext) VALUES (?, ?, ?)', ('Todo1', 'homework', 'Do homework'))
    db.commit()
    return jsonify('Success!')