from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from app.models.entry import Title, Entry
from app.forms.entry import CreateEntryForm
from app.services.entry import EntryService

entry = Blueprint('entry', __name__, url_prefix='/entry')


@entry.route('/')
@entry.route('/<int:page>')
def index(page=1):
    titles = Title.query.filter_by(is_active=True).order_by(Title.created_at.desc()).paginate(page, 5, False)
    return render_template('views/entry/index.html', title='All Entrys', titles=titles)


@entry.route('/<string:title>', methods=['GET', 'POST'])
@login_required
def create(title):
    service = EntryService()
    title_object = service.get_title(title)
    form = CreateEntryForm()

    if title_object and request.method != 'POST':
        return render_template(
            'views/entry/title_detail.html',
            title=title_object.name, form=form, entrys=title_object.entrys)

    if form.validate_on_submit():
        service.create_entry(title, form.entry.data, current_user)

        flash('Entry Successfully Added', 'success')
        return redirect(url_for('entry.create', title=title))

    return render_template('views/entry/title_create.html', title=title, form=form)