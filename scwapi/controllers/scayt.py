# -*- coding: utf-8 -*-
import json
import re
import collections
from tg import expose, redirect, validate, flash, url
from scwapi.lib.base import BaseController
from os import path
from faspell import spell_checker
import scwapi
from messenger.messenger import Messenger


dictionary_filename = path.abspath(path.join(path.dirname(scwapi.__file__), '..', 'database', 'dictionary'))

global words_dictionary


class Dictionary(object):
    def __init__(self, filename):
        self.database = filename
        self.load()

    def add_word(self, word):
        words_dictionary[word] = 1
        self.dump(word)

    def dump(self, word):
        with open(self.database, 'a', encoding='utf-8') as dictionary:
            dictionary.write('%s%s' % ('\n', word))

    def words(self, database):
        return re.split('\n', database)

    def train(self, words):
        return dict.fromkeys(words, 1)

    def load(self):
        try:
            if not words_dictionary:
                with open(self.database, 'r', encoding='utf-8') as my_file:
                    return self.train(self.words(my_file.read()))
            else:
                return words_dictionary
        except NameError:
                with open(self.database, 'r', encoding='utf-8') as my_file:
                    return self.train(self.words(my_file.read()))


words_dictionary = Dictionary(dictionary_filename).load()


class SCAYTController(BaseController):
    @expose('scwapi.templates.scayt.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    def get_lang_list(self):

        return {
            "langList": {
                "ltr": {"en_US": "Persian"},
                "rtl": {}
            },
            "verLang": 6
        }

    def get_banner(self):
        return {
            "undefined": True
        }

    def add_to_dictionary(self, text):
        try:
            my_dictionary = Dictionary(dictionary_filename)
            my_dictionary.add_word(text)
            return {
                'Ok': True,
                'error': None
            }

        except Exception as ex:
            crow = Messenger(str(ex))
            return crow.deliver()

    def check_spelling(self, text):
        check = spell_checker.SpellChecker(words_dictionary)
        return check.correct(text)

    @expose('json')
    def ssrv(self, cmd=None, callback=None, **kwargs):

        if cmd == 'get_lang_list':
            result = self.get_lang_list()
        elif cmd == 'getbanner':
            result = self.get_banner()
        elif cmd == 'check_spelling':
            result = self.check_spelling(kwargs.get('text'))
        elif cmd == 'add_to_dictionary':
            return self.add_to_dictionary(kwargs.get('text'))
        else:
            raise Exception('The requested operation not implemented yet.')

        return '%s(%s)' % (callback, json.dumps(result))
