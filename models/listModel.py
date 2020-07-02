# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\models\listModel.py
# Compiled at: 2020-07-01 16:30:57
# Size of source mod 2**32: 1173 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel
from lib import contactsHandler
from lib import settingsHandler
import lib.functionEngine as functions

class ListModel(BaseModel):
    """''"""

    def __init__(self, filenames, debug):
        super(ListModel, self).__init__(filenames, debug)
        self.debug = debug
        if self.debug:
            print('ListModel: __init__')
        self.listboxEnabled_values = []
        self.listboxDisabled_values = []
        self.load_listbox_values()

    def load_listbox_values(self):
        if self.debug:
            print('ListModel: load_listbox_values()')
        for name in self.xml_contacts.get_enable_list('contact', 'name'):
            self.listboxEnabled_values.append(name)
        else:
            for name in self.xml_contacts.get_disable_list('contact', 'name'):
                self.listboxDisabled_values.append(name)