import os
APP_CONFIG = "/home/spellchecker/workspace/spell_checker_web_api/production.ini"

#Setup logging
import logging.config
logging.config.fileConfig(APP_CONFIG)

#Load the application
from paste.deploy import loadapp
application = loadapp('config:%s' % APP_CONFIG)

