import re
import RemmeMethods


class Token:

    def __init__(self, rest):
        self.rest = rest
        self.method = RemmeMethods.Methods()

    def get_balance(self, key):
        pattern = '^[0-9a-f]{66}$'
        if re.search(pattern, key) is None:
            raise Exception("Not correct address")
        else:
            res = self.rest.get_rest(self.method.token, key)
            return res

    def transfer(self, key, value):
        pattern = '^[0-9a-f]{66}$'
        if re.search(pattern, key) is None:
            raise Exception("Not correct address")
        if value <= 0:
            raise Exception("Not correct Pay value")
        else:
            payload = {"amount": value, "pub_key_to": key}
            res = self.rest.post_rest(self.method.token, payload)
            return res

