import smtlib 




class Email:
    
    def __init__(self, theme, body):
        
        self.sender_mail = 'mailsne'
        self.sender_password = 'sd'
        
        self.smtpsession = smtplib.SMTP('smtp.gmail.com',587)
        self.smtpsession.starttls()
        
        self.smtpsession.login(self.sender_mail, 'mail sendr pass')

        self.theme = theme
        self.body = body
        
        return self

    
    def to_many_contact(self, receiver):
        pass
    
    def to_single(self, receiver):
        
        
    
    def send(self):
        pass