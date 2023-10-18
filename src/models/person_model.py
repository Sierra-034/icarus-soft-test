from sqlalchemy.event import listen
from models.sqlalchemy_instance import db

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), unique=True, nullable=False)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False


def insert_names(*args, **kwargs):
    names = [
        'denise smith',
        'amanda robbins',
    ]

    for name in names:
        person_instance = Person(nombre_completo=name)
        db.session.add(person_instance)

listen(Person.__table__, 'after_create', insert_names)
