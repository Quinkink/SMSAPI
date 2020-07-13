"""
Created on 17 Mar 2020

@author: Eleonore
"""
from lib import contactsHandler
from lib import settingsHandler
from lib import stringsHandler


class BaseModel:
    """
    """
    def __init__(self, filenames, debug):
        """

        :param filenames: (dictionary) contains XML file names
        :param debug:
        """
        self.debug = debug
        if self.debug:
            print('BaseModel: __init__')
        self.filenameContacts = filenames['contacts']
        self.filenameSettings = filenames['settings']
        self.filenameLanguage = filenames['language']

        # PLACE HOLDERS FOR FILE DATA
        self.xml_contacts = None
        self.xml_settings = None
        self.xml_strings = None

        # self.settings = {}
        self.settings = {}
        self.contacts = {}
        self.strings = {}

        # LOAD VALUES
        self.load_xml_settings()
        self.load_xml_contacts()

    def load_xml_settings(self):
        if self.debug:
            print('BaseModel: load_xml_settings()')
            print('filename : ' + self.filenameSettings)
        self.xml_settings = settingsHandler.XMLSettingsHandler(self.filenameSettings, self.debug)
        self.settings = self.xml_settings.get_dictionary()
    
    def load_xml_contacts(self):
        if self.debug:
            print('BaseModel: load_xml_contacts()')
            print('filename : ' + self.filenameContacts)
        self.xml_contacts = contactsHandler.XMLContactsHandler(self.filenameContacts, self.debug)
        # self.contacts = self.xml_contacts.get_dictionary()

    def load_xml_strings(self, view):
        if self.debug:
            print('AppModel: load_xml_strings()')
            print('AppModel: filenameLanguage : ' + self.filenameLanguage)
        self.xml_strings = stringsHandler.XMLStringsHandler(self.filenameLanguage, self.debug)
        self.strings = self.xml_strings.get_dictionary(view)
        if self.debug:
            print('appModel: strings')
            print(self.strings)

    def load_contact(self, place_holder):
        if self.debug:
            print('BaseModel: load_contact()')
        pass
