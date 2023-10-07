import secrets

class KMS:
    def __init__(self):
        self.TEK = secrets.token_bytes(16)
        self.dic = {"KMS": self.TEK}

    def update(self, count):
        print(count)
        self.dic[count] = secrets.token_bytes(16)

    def getTEK(self):
        return self.TEK
    
    def getDic(self):
        return self.dic

class Client(KMS):
    __count = 1
    def __init__(self, KMS):
        self.TEK = KMS.getTEK()
        self.dic = KMS.getDic()
        super().update(Client.__count)
        Client.__count += 1

kms = KMS()
u1 = Client(kms)
print(kms.getDic())
print(u1.getDic())