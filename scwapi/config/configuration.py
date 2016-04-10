from pymlconf import ConfigManager


__builtin_config = """

receiving_channel: '@amin'
crow_api_url: 'http://crow.farakav.com/api/message'
slack_access_token: xoxp-13319976114-20556087794-31577611078-8f47cd840d

"""

settings = None


def init():
    global settings
    settings = ConfigManager(__builtin_config)
    return settings