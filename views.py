from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from db_models import Note
from __init__ import my_database
import json

views = Blueprint('/views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Content is required', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            my_database.session.add(new_note)
            my_database.session.commit()
            flash('Note added', category='success')


    return render_template("home.html", user=current_user)

@views.route('/edit', methods = ['POST'])
@login_required

def edit():
    note_id = request.form.get('note_id')
    note_data = request.form.get('note_data')
    if len(note_data) < 1:
        flash('Content is required', category='error')
    else:
        note = Note.query.filter_by(id=note_id).first()
        note.data = note_data
        my_database.session.commit()
        flash('Note updated', category='success')

    return jsonify({'status': 'ok'})

    
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            my_database.session.delete(note)
            my_database.session.commit()

    return jsonify({})