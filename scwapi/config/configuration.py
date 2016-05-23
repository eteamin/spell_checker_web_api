from pymlconf import ConfigManager


__builtin_config = """

receiving_channel: '@amin'
crow_api_url: 'http://crow.farakav.com/api/message'

"""

settings = None


def init():
    global settings
    settings = ConfigManager(__builtin_config)
    return settings