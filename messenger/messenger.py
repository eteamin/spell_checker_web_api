from scwapi.config import configuration
import requests


class Messenger(object):
    def __init__(self, text):
        configuration.init()
        self.token = 'xoxp-13319976114-20556087794-31577611078-8f47cd840d'
        self.text = text
        self.receiving_channel = '@amin'

        self.message = {
                'token': self.token,
                'text': self.text,
                'channel': self.receiving_channel
        }

    def deliver(self):
        response = requests.post('http://crow.farakav.com/api/message', json=self.message)
        return response.json()