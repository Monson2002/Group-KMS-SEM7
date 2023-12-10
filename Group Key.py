import secrets
import time
class KeyManagementServer:
    def __init__(self):
        self.keys = {}
        # self.generate_key = self.generate_key()  # Generate a new group key
        self.user_keys = {}  # Dictionary to store user keys
        self.keys["KMS"] = self.generate_key()
        self.keys["Users"] = self.user_keys

    def get_keys(self):
        return self.keys

    def get_generate_key(self):
        return self.generate_key

    def get_user_key_store(self, username):
        dic = {}
        dic["KMS"] = self.keys["KMS"]
        for key,value in self.user_keys.items():
            if key == username:
                pass
            else:
                dic[key] = value
        return dic

    def get_user_keys(self):
        if self.user_keys:
            return self.user_keys
        else:
            return None

    def generate_key(self):
        # Generate a random key
        key = secrets.token_urlsafe(16)
        return key

    def add_user(self, username):
        # Generate a new user key
        user_key = self.keys["KMS"]
        
        # Update the group key
        self.keys["KMS"] = self.generate_key()
        # Update the user key store
        for key,value in self.user_keys.items():
            self.user_keys[key] = self.generate_key()

        # Store the user key in the dictionary
        self.user_keys[username] = user_key

    def remove_user(self, username):
        # Remove the user and their key from the user_keys dictionary
        if username in self.user_keys:
            del self.user_keys[username]

        # Update the group key when a user leaves
        self.keys["KMS"] = self.generate_key()
        # Update the user key store
        for key,value in self.user_keys.items():
            self.user_keys[key] = self.generate_key()

start = time.perf_counter()
kms = KeyManagementServer()

print("Added KMS : ")
print(kms.get_keys())

print("",end="\n\n")

kms.add_user("user1")
print("Added User1 : ")
print(kms.get_keys())
for userName,userValue in kms.user_keys.items():
    print(userName,end=" :> ")
    print(kms.get_user_key_store(userName))
print("",end="\n\n")

kms.add_user("user2")
print("Added User2 : ")
print(kms.get_keys())
for userName,userValue in kms.user_keys.items():
    print(userName,end=" :> ")
    print(kms.get_user_key_store(userName))
print("",end="\n\n")

kms.add_user("user3")
print("Added User3 : ")
print(kms.get_keys())
for userName,userValue in kms.user_keys.items():
    print(userName,end=" :> ")
    print(kms.get_user_key_store(userName))
print("",end="\n\n")

kms.add_user("user4")
print("Added User4 : ")
print(kms.get_keys())
for userName,userValue in kms.user_keys.items():
    print(userName,end=" :> ")
    print(kms.get_user_key_store(userName))
print("",end="\n\n")

kms.remove_user("user2")
print("Removed User2 : ")
print(kms.get_keys())
for userName,userValue in kms.user_keys.items():
    print(userName,end=" :> ")
    print(kms.get_user_key_store(userName))
print("",end="\n\n")

kms.add_user("user2")
print("Added User2 : ")
print(kms.get_keys())
for userName,userValue in kms.user_keys.items():
    print(userName,end=" :> ")
    print(kms.get_user_key_store(userName))
print("",end="\n\n")

end = time.perf_counter()

print(f"Total Time Taken : {((end-start) * 10**6):.02f} micro seconds")