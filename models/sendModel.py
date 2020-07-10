"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel


class SendModel(BaseModel):
    """''"""

    def __init__(self, filenames, debug):
        super(SendModel, self).__init__(filenames, debug)
        self.debug = debug
        if self.debug:
            print('SendModel: __init__')
        self.spinbox_values = []

        self.load_xml_strings('SEND')
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