# -*- coding: utf-8 -*-
import json
from tg import expose, redirect, validate, flash, url
from scwapi.lib.base import BaseController
from persian_spell_checker import spell_checker
from os import path
import scwapi

dictionary_filename = path.abspath(path.join(path.dirname(scwapi.__file__), '..', 'database', 'dictionary'))
# from scwapi.model import DBSession


class SCAYTController(BaseController):
    @expose('scwapi.templates.scayt.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    def get_lang_list(self):
        return {
            "langList": {
                "ltr": {"fa_IR": "Persian"},
                "rtl": {}
            },
            "verLang": 6
        }

    def get_banner(self):
        return {
            "undefined": True
        }

    def check_spelling(self, text):
        with open(dictionary_filename, 'r', encoding='utf8') as my_file:
            check = spell_checker.SpellChecker(my_file.read())
            return check.correct(text)

    @expose('json')
    def ssrv(self, cmd=None, callback=None, **kwargs):

        if cmd == 'get_lang_list':
            result = self.get_lang_list()
        elif cmd == 'getbanner':
            result = self.get_banner()
        elif cmd == 'check_spelling':
            result = self.check_spelling(kwargs.get('text'))
        else:
            raise Exception('The requested operation not implemented yet.')

        return '%s(%s)' % (callback, json.dumps(result))

