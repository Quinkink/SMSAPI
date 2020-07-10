"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel


class EditModel(BaseModel):
    """''"""

    def __init__(self, filenames, debug):
        super(EditModel, self).__init__(filenames, debug)
        self.debug = debug
        if self.debug:
            print('EditModel: __init__')
        self.contact = {'id': '',
                        'name': '',
                        'user': '',
                        'code': '',
                        'enable': self.settings['defaultContactEnable']}

        self.load_xml_strings('EDIT')

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