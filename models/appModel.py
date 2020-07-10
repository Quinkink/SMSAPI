"""
Created on 17 Mar 2020

@author: Eleonore
"""
from lib import settingsHandler
from lib import stringsHandler
import lib.functionEngine as functions


class AppModel(object):
    """
    """
    def __init__(self, filename):
        """
        :param filename: (string) contains XML file name
        """
        # LOAD PLACE HOLDERS
        self.debug = False
        self.xml_settings = None
        self.xml_strings = None
        self.settings = {}
        self.strings = {}

        self.filenameSettings = functions.find_data_file(filename, 'data')

        # LOAD VALUES
        self.load_xml_settings()
        if self.settings['debug'] == "True":
            self.debug = True
        else: self.debug = False

        if self.debug:
            print(self.debug)
            print('AppModel: __init__ (after settings loaded)')
            print('AppModel: filename : ' + self.filenameSettings)
            print('AppModel: load_xml_settings() (after xml_settings were loaded)')

        self.filenameContacts = functions.find_data_file(self.settings['filenameContacts'], 'data')
        self.filenameLanguage = functions.find_data_file(self.settings['filenameLanguage'], 'data')
        self.load_xml_strings()
          
    def load_xml_settings(self):
        self.xml_settings = settingsHandler.XMLSettingsHandler(self.filenameSettings, self.debug)
        self.settings = self.xml_settings.get_dictionary()

    def load_xml_strings(self):
        if self.debug:
            print('AppModel: load_xml_strings()')
            print('AppModel: filenameLanguage : ' + self.filenameLanguage)
        self.xml_strings = stringsHandler.XMLStringsHandler(self.filenameLanguage, self.debug)
        self.strings = self.xml_strings.get_dictionary('APP')
        if self.debug:
            print('appModel: strings')
            print(self.strings)
