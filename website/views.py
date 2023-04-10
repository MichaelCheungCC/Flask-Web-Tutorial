from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, To_do
from . import db
import json
import pytz
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        category = request.form.get('category')
        note = request.form.get('note')
        if not category:
            flash('Please select a category!', category='error')
        elif len(note) < 1:
            flash('Please enter something in the note!', category='error')
        else:
            new_note = Note(category=category, data=note, user_id=current_user.id, date=pytz.timezone('Asia/Shanghai').localize(datetime.now()))
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/to-do', methods=['GET', 'POST'])
@login_required
def to_do():
    if request.method == 'POST':
        due_date_str = request.form.get('due_date')
        to_do = request.form.get('to-do')
        
        if len(due_date_str) < 1:
            flash('Please select a date.', category='error')
        elif len(to_do) < 1:
            flash('Please enter something.', category='error')

        else:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            new_to_do = To_do(data=to_do, user_id=current_user.id, date=pytz.timezone('Asia/Shanghai').localize(datetime.now()), due_date=due_date)
            db.session.add(new_to_do)
            db.session.commit()
            flash('To-Do added!', category='success')   

    return render_template("to_do_list.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/delete-to-do', methods=['POST'])
def delete_to_do():
    to_do = json.loads(request.data)
    todoID = to_do['todoID']
    to_do = To_do.query.get(todoID)
    if to_do:
        if to_do.user_id == current_user.id:
            db.session.delete(to_do)
            db.session.commit()
    return jsonify({})