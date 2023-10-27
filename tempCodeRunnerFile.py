r_key_store(self, username):
        dic = {}
        dic["KMS"] = self.generate_key
        for key,value in self.user_keys.items():
            if key == username:
                pass
            else:
                dic[key] = value
        return dic