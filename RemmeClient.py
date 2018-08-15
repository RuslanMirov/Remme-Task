import RemmeToken
import RemmeRest


class Client:

    def __init__(self, key=None, config=None):
        self.key = key
        if config is None:
            self.config = {"node_address": "localhost", "socket_port": "9080", "api_port": "8080", "validator_port": "8008", "ssl_mode": False}
        else:
            self.config = config
        self.__rest = RemmeRest.Rest(self.config)
        self.token = RemmeToken.Token(self.__rest)








