from app.models.models import Base, Contact
from app.db.db import Session


class ContactHandler:
    
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        
    def create_new_contact(name:str, email:str):
        session = Session()
        contact = Contact(name = name, email = email)
        session.add(contact)
        session.commit()
        session.close()
        return True
    
    @staticmethod
    def get_contacts():
        session = Session()
        contacts = session.query(Contact).all()
        session.close()
        return contacts
    
    @staticmethod
    def get_contact_by_id(id):
        session = Session()
        contact = session.query(Contact).get(id)
        session.close()
        return contact
        
    @staticmethod
    def update_contact( id, name = None , email = None):
        session = Session()
        contact = session.query(Contact).get(id)
        if name is not None:
            contact.name = name
        if email is not None:
            contact.email = email
        session.commit()
        session.close()
        return True
    
    @staticmethod
    def destroy_contact( id):
        session = Session()
        contact = session.query(Contact).get(id)
        session.delete(contact)
        session.commit()
        session.close()
        return True
    
    
    