"""
Created on 17 Mar 2020

@author: Eleonore
"""
from lib import contactsHandler
from lib import settingsHandler
import lib.functionEngine as functions


class BaseModel:
    """
    """
    def __init__(self, filenames, debug):
        self.debug = debug
        if self.debug:
            print('BaseModel: __init__')
        self.filenameContacts = functions.find_data_file(filenames['contacts'], 'data')
        self.filenameSettings = functions.find_data_file(filenames['settings'], 'data')

        # PLACE HOLDERS FOR FILE DATA
        self.xml_contacts = None
        self.xml_settings = None

        # self.settings = {}
        self.settings = {}
        self.strings = {}

        # LOAD VALUES
        self.load_xml_contacts()
        self.load_xml_settings()
    
    def load_xml_contacts(self):
        if self.debug:
            print('BaseModel: load_xml_contacts()')
        if self.debug:
            print('filename : ' + self.filenameContacts)
        self.xml_contacts = contactsHandler.XMLContactsHandler(self.filenameContacts, self.debug)
          
    def load_xml_settings(self):
        if self.debug:
            print('BaseModel: load_xml_settings()')
        if self.debug:
            print('filename : ' + self.filenameSettings)
        self.xml_settings = settingsHandler.XMLSettingsHandler(self.filenameSettings, self.debug)
        self.settings = self.xml_settings.get_dictionary('setting', 'value')
        self.strings = self.xml_settings.get_dictionary('string', 'value')

        if self.debug:
            pass
            print(self.settings)
            print(self.strings)

    def load_contact(self, place_holder):
        if self.debug:
            print('BaseModel: load_contact()')
        pass
