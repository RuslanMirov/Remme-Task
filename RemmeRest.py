import requests


class Rest:
    def __init__(self, config):
        self.config = config

    def url(self, method, url_parameter=None, query_parameter=None):
        ssl_mode = "https://" if self.config["ssl_mode"] else "http://"
        if url_parameter is not None:
            if query_parameter is None:
                url = ssl_mode + self.config['node_address'] + ":" + self.config['api_port'] + method + "/" + url_parameter
            else:
                url = ssl_mode + self.config['node_address'] + ":" + self.config['api_port'] + method + "/" + url_parameter + query_parameter
        else:
            url = ssl_mode + self.config['node_address'] + ":" + self.config['api_port'] + method
        return url

    def delete_rest(self, method, payload):
        url = self.url(method)
        response = requests.delete(url, json=payload)
        return response.json()

    def get_rest(self, method, url_parameter, query_parameter=None):
        url = self.url(method, url_parameter, query_parameter)
        response = requests.get(url)
        return response.json()

    def post_rest(self, method, payload):
        url = self.url(method)
        response = requests.post(url, json=payload)
        return response.json()

    def put_rest(self, method, payload):
        url = self.url(method)
        response = requests.put(url, json=payload)
        return response.json()
