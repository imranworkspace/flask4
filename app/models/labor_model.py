from app.extentions import db

class LaborsModels(db.Model):
    __tablename__='labors'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email
        }