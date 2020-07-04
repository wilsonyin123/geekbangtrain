from sqlalchemy import Column, Integer, String, Float
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from manage import db
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)


# 使用装饰器完成password的读取和写入功能分离
    @property
    def password(self):
        return None
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
  
    def is_active(self):
        return True