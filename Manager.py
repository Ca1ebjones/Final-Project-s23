from cryptography import Crypt
import random
import string
import json
import sys
class Manager:
    def __init__(self, file_name="passwords.txt"):
        self.key=self.generate_key()
        self.crypt=Crypt(self.key)
        self.safe={}

    def generate_key(self):
        char_list=string.ascii_letters+string.digits
        length=random.randint(5,10) 
        key="".join(random.choice(char_list) for i in range(length))
        return key
    
    def generate_password(self,site,usr,length): 
        char_list=string.ascii_letters+string.digits+"@$"
        password="".join(random.choice(char_list) for i in range(length))
        account={usr:password}
        self.safe[site]= account
        return password

    def get_password(self,site,usr):
        account= self.safe[site]
        pas=account[usr]
        return pas
    def delete (self,site,usr):
        account=self.safe[site]
        account.pop(usr)
        self.safe=account
    def update(self,site,usr,pas):
        account= self.safe[site]
        account[usr]=pas
        self.safe[site]=account
    def save(self):
        file=open("passwords.txt",'w')
        file.write(json.dumps(self.safe))
    def load (self):
        file=open("passwords.txt", 'r')
        data=file.read()
        self.safe=json.loads(data)
        return self.safe