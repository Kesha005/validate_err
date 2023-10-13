
    
from cryptography.fernet import Fernet


class KeyGenerator:
    
    def generate_key():
        key = Fernet.generate_key
        with open("ch.key", "wb") as filekey:
            filekey.write(key)
        
        return key
    
    
    
    def return_key():
        with open('ch.key', 'rb') as filekey:
            key = filekey.read()
        
        if(key != ''):
            pass
        else:
            key = self.generate_key()
        
        fernet = Fernet(key)
        return fernet 
 


class Chiper:
    
    def encrypt_data(self, data):
        
        token = self.return_key().encrypt(data.encode())
        return token 
    
    
    def decrypt_data(self, data):
        token = self.return_key().decrypt(data)
        
        return token.decode()
    