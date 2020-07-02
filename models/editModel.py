# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\models\editModel.py
# Compiled at: 2020-07-01 16:30:57
# Size of source mod 2**32: 1346 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel
from lib import contactsHandler
from lib import settingsHandler
import lib.functionEngine as functions

class EditModel(BaseModel):
    """''"""

    def __init__(self, filenames, debug):
        super(EditModel, self).__init__(filenames, debug)
        self.debug = debug
        if self.debug:
            print('EditModel: __init__')
        self.contact = {'id':'', 
         'name':'', 
         'user':'', 
         'code':'', 
         'enable':self.settings['defaultContactEnable']}

    def load_contact(self, contact_name):
        if self.debug:
            print('EditModel: load_contact()')
            print(contact_name)
        self.contact = self.xml_contacts.get_element('contact', 'name', contact_name)
        if self.debug:
            print(self.contact)

    def save_contact(self, contact):
        if self.debug:
            print('save_contact()')
        return self.xml_contacts.append_to_list(contact)