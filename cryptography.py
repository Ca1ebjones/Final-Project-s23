class Crypt:
    def __init__ (self, key):
        self.key= key
    
    def encrypt(self, msg):
        msg=msg+ self.key
        encrypt_msg=""
        for index,letter in enumerate(msg):
            if index %2==0:
                encrypt_msg=encrypt_msg+self.shift_up(letter, index)  
            else:
                encrypt_msg=encrypt_msg+self.shift_down(letter, index)
        return encrypt_msg
    def shift_up(self,letter,index):
        asci= ord(letter)
        shift=ord(self.key[index%len(self.key)])
        asci=asci+shift
        while asci>122:
            asci=asci-122+32
        return chr(asci)
    def shift_down(self,letter,index):
        asci= ord(letter)
        shift=ord(self.key[index%len(self.key)])
        asci=asci-shift
        while asci<33:
            asci=123-33 + asci
        return chr(asci)