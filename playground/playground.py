import requests


class PlayGround(object):
    def get_google(self):
        return requests.get('https://www.google.com/')
