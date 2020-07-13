"""
Created on 17 Mar 2020

@author: Eleonore
"""
from models.baseModel import BaseModel
import lib.functionEngine as functions


class AppModel(BaseModel):
    """
    """
    def __init__(self, filenames, debug=False):
        """

        :param filenames: (dictionary) contains XML file names
        :param debug:
        """
        super(AppModel, self).__init__(filenames, debug)
        # SETTINGS FROM FILE & LOAD VALUES
        self.load_xml_settings()
        if self.settings['debug'] == "True":
            debug = True
            print(self.debug)
            print('AppModel: __init__ (after settings loaded)')
            print('AppModel: filename : ' + self.filenameSettings)
            print('AppModel: load_xml_settings() (after xml_settings were loaded)')
            print('AppModel: invoking Super __init__')
        else:
            debug = False

        self.filenameContacts = functions.find_data_file(self.settings['filenameContacts'], 'data')
        self.filenameLanguage = functions.find_data_file(self.settings['filenameLanguage'], 'data')

        # LOAD PLACE HOLDERS
        self.load_xml_strings('APP')
