from app import db
from app.models.abstract import BaseModel


class Title(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    is_active = db.Column(db.Boolean(), default=True)
    entrys = db.relationship('Entry', backref='entrys', lazy=True)

    def __repr__(self):
        return "Title({})".format(self.name)


class Entry(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=False)
    title = db.relationship('Title', backref="title")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref="entrys")
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "Entry({}: {})".format(self.title, self.content[15:])