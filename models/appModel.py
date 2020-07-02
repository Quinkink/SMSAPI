"""
Created on 17 Mar 2020

@author: Eleonore
"""
from lib import contactsHandler
from lib import settingsHandler
import lib.functionEngine as functions


class AppModel(object):
    """
    """
    def __init__(self, filename, debug):
        """

        :param filename: (string) contains XML file name
        :param debug: (boolean)
        """
        self.debug = debug
        if self.debug:
            print('ListModel __init__')
        self.filename = functions.find_data_file(filename, 'data')
        self.xml_settings = None
        self.menu = {}
        self.settings = {}
        self.strings = {}

        # LOAD VALUES
        self.load_xml_settings()
          
    def load_xml_settings(self):
        if self.debug:
            print('load_xml_settings()')
        if self.debug:
            print('filename : ' + self.filename)
        self.xml_settings = settingsHandler.XMLSettingsHandler(self.filename, self.debug)
        self.settings = self.xml_settings.get_dictionary('setting', 'value')
        self.strings = self.xml_settings.get_dictionary('string', 'value')

        if self.debug:
            print(self.settings)
            print(self.strings)
