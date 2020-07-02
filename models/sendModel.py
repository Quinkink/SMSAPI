# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\models\sendModel.py
# Compiled at: 2020-07-01 16:30:57
# Size of source mod 2**32: 1207 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel
from lib import contactsHandler
from lib import settingsHandler
import lib.functionEngine as functions

class SendModel(BaseModel):
    """''"""

    def __init__(self, filenames, debug):
        super(SendModel, self).__init__(filenames, debug)
        self.debug = debug
        if self.debug:
            print('SendModel: __init__')
        self.spinbox_values = []
        self.load_spinbox_values()

    def load_spinbox_values(self):
        if self.debug:
            print('load_spinbox_values()')
        contactsList = self.xml_contacts.get_enable_list('contact', 'name')
        if len(contactsList) > 0:
            self.spinbox_values = [
             self.strings['spinboxDefault']]
            for x in contactsList:
                self.spinbox_values.append(x)

        else:
            self.spinbox_values = [
             self.strings['spinboxEmpty']]