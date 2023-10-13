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
        
        self.receivers = []
        return self

    
    def to_many_contact(self, receivers):
        
        for receiver in receivers:
            self.receivers.append(receiver)
            
        return self
    
    def to_single(self, receiver):
        self.receivers.append(receiver)
        
        return self
        
    
    def send(self):
        
        self.smtpsession.sendmail(
            self.sender_mail,
            self.receivers,
            self.body
        )