import requests

class HTTP:
    @staticmethod
    def get( url, return_json = True):
        r = requests.get(url) # return the result of request of url
        # r is a packaged object
        # return json format object
        if r.status_code == 200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            return {} if return_json else ''

