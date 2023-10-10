
class KeyManagementServer:
    def __init__(self):
        self.keys = {}
        self.group_key = self.generate_key()  # Generate a new group key
        self.user_keys = {}  # Dictionary to store user keys
        self.keys["KMS"] = self.group_key,1
        self.keys["Users"] = self.user_keys

    def get_keys(self):
        return self.keys

    def get_group_key(self):
        return self.group_key

    def get_user_key(self, username):
        if username in self.user_keys:
            return self.user_keys[username]
        else:
            return None

    def get_user_keys(self):
        if self.user_keys:
            return self.user_keys
        else:
            return None

    def generate_key(self):
        # Generate a new random key (you should use a secure method for key generation)
        import random
        import string
        key_length = 16  # Change this to your desired key length
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(key_length))

    def add_user(self, username):
        # Generate a new user key
        user_key = self.generate_key()
        
        # Update the group key
        self.group_key = self.generate_key()
        self.keys["KMS"] = self.group_key

        # Store the user key in the dictionary
        self.user_keys[username] = user_key

    def remove_user(self, username):
        # Remove the user and their key from the user_keys dictionary
        if username in self.user_keys:
            del self.user_keys[username]

        # Update the group key when a user leaves
        self.keys["KMS"] = self.generate_key()

# Example usage:
kms = KeyManagementServer()
print(kms.get_keys())

# Add a new user

kms.add_user("user1")
print(kms.get_keys())
kms.add_user("user2")

print(kms.get_keys())
kms.remove_user("user2")
print(kms.get_keys())
