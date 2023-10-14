from app.models.models import Base, Password
from app.db.db import Session
from app.handler.chiper import Chiper

class PasswordHandler:
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
    
    def store(self):
        session = Session()
        new_password = Password(
            name = self.name,
            email = self.email,
            username = self.username,
            password = Chiper.encrypt_data(self.password)    
        )
        session.add(new_password)
        session.commit()
        session.close()
        return True
    
    @staticmethod
    def get_password():
        session = Session()
        passwords = session.query(Password).get()
        decrypted =Chiper.decrypt_data_in_object_array(passwords)
        return decrypted
    
    @staticmethod
    def by_like_name(name:str):
        session = Session()
        search = "%{}%".format(name)
        passwords = session.query(Password).filter(
            Password.name.like(search)
            ).all()
        session.close()
        decrypted =Chiper.decrypt_data_in_object_array(passwords)
        return decrypted
    
    
        
        
    

