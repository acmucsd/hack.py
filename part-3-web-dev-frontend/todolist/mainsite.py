from flask import Blueprint, render_template, request
from datetime import datetime
from .forms import TodoForm, DeleteForm

bp = Blueprint('mainsite', __name__, url_prefix='/')

todolist = [{"item": "abcd", "type": "todo", "description": "oaisdfasf"}]

@bp.route('/', methods=['GET', 'POST', 'DELETE'])
def hello():
    print(request.method)
    form = TodoForm()
    deleteForm = DeleteForm()
    if request.method == 'POST':
        if request.form.get('submit') == 'Add Item':
          todolist.append({"item": form.item.data, "type": form.type.data, "description": form.description.data})
        elif len(todolist) != 0:
          todolist.pop()
    return render_template('todolist.html', todolist=todolist, datetime=datetime, form=form, deleteForm=deleteForm)