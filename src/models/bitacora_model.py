from models.sqlalchemy_instance import db

class Bitacora(db.Model):
    __tablename__ = 'bitacora'

    id = db.Column(db.Integer, primary_key=True)
    params = db.Column(db.String(100), nullable=False)
    response = db.Column(db.Boolean, default=False)
    date_time = db.Column(db.DateTime(), default=db.func.current_timestamp())

    @classmethod
    def new_bitacora(cls, **kwargs):
        return Bitacora(**kwargs)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
        
    def __repr__(self) -> str:
        return f'{self.params}, {self.response}, {self.date_time}'
