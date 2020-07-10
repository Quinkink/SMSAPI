"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel


class ListModel(BaseModel):
    """''"""

    def __init__(self, filenames, debug):
        super(ListModel, self).__init__(filenames, debug)
        self.debug = debug
        if self.debug:
            print('ListModel: __init__')
        self.listboxEnabled_values = []
        self.listboxDisabled_values = []

        self.load_xml_strings('LIST')
        self.load_listbox_values()

    def load_listbox_values(self):
        if self.debug:
            print('ListModel: load_listbox_values()')
        for name in self.xml_contacts.get_enable_list('contact', 'name'):
            self.listboxEnabled_values.append(name)
        else:
            for name in self.xml_contacts.get_disable_list('contact', 'name'):
                self.listboxDisabled_values.append(name)
