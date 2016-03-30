import os
APP_CONFIG = "/home/amin/workspace/spell_checker_web_api/production.ini"
#os.environ['PYTHON_EGG_CACHE'] = '/usr/local/turbogears/python-eggs'

#Setup logging
import logging.config
logging.config.fileConfig(APP_CONFIG)

#Load the application
from paste.deploy import loadapp
application = loadapp('config:%s' % APP_CONFIG)

