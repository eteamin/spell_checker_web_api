# -*- coding: utf-8 -*-
import json
import re
import collections
from tg import expose, redirect, validate, flash, url
from scwapi.lib.base import BaseController
from os import path
from faspell import spell_checker
import scwapi

dictionary_filename = path.abspath(path.join(path.dirname(scwapi.__file__), '..', 'database', 'dictionary'))
# from scwapi.model import DBSession

global words_dictionary


class Dictionary(object):
    def __init__(self, database):
        self.word_list_database = self.train(self.words(database))

    def words(self, database):
        return re.split('\n', database)

    def train(self, features):
        model = dict.fromkeys(features, 1)
        return model


def load_dictionary():
    try:
        if not words_dictionary:
            return
    except NameError:
        with open(dictionary_filename, 'r') as my_file:
            return Dictionary(my_file.read())

words_dictionary = load_dictionary()


# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls._instance, cls):
#             cls._instance = object.__new__(cls, *args, **kwargs)
#         return cls._instance

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
        global words_dictionary
        check = spell_checker.SpellChecker(words_dictionary.word_list_database)
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
