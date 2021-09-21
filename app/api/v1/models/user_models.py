from app import db


class Customer (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phonenumber = db.Column(db.String(255), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        pass_hash = (password)
        self.password = pass_hash

    def check_password(self, password):
        return (self.password, password)

    def __repr__(self):
        return f'User: {self.username}'


class Pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))


    def __repr__(self):
        return f'User {self.name}'   

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255)) 
    location = db.Column(db.String(255))  

class Orders(db.Model):
    __tablename__ = 'orders' 

    id = db.Column(db.Integer,primary_key = True)
    number = db.Column(db.String(255))
    details = db.Column(db.String(255))       