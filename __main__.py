import RemmeClient
import time

default_config = {"node_address": "localhost", "socket_port": "9080", "api_port": "8080", "validator_port": "8008", "ssl_mode": False}
key = ""

if __name__ == '__main__':

    # Transfer and balance test
    client = RemmeClient.Client(key, default_config)

    beforeBalance = client.token.get_balance("0317324bdff36038b32646d078f538243e1d1e81b297d03692f672986ec4e10381")
    print("beforeBalance ", beforeBalance)

    client.token.transfer("0317324bdff36038b32646d078f538243e1d1e81b297d03692f672986ec4e10381", 1000)

    time.sleep(2)
    balanceAfter = client.token.get_balance("0317324bdff36038b32646d078f538243e1d1e81b297d03692f672986ec4e10381")
    print("balanceAfter ", balanceAfter)

