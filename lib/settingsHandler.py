import xml.etree.ElementTree as ElementTree


class XMLSettingsHandler(object):
    """

    """
    def __init__(self, file, debug=True):
        """

        :param file:
        :param debug:
        """
        self.debug = debug
        if self.debug:
            print('XMLSettingsHandler: __init__')
        self.file = file
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
        if self.debug:
            print('root tag : ' + self.root.tag)
        
        # XML SettingsFrame
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
    
    def get_dictionary(self):
        """
        :return: (dictionary) dictionary)
        """
        # returns XML Settings file as a python dictionary (associative array)
        dictionary = {}
        for elem in self.tree.iterfind('setting'):
            dictionary[elem.get('key')] = elem.get('value')
        if self.debug:
            print(dictionary)
        return dictionary
        
    # def update_settings(self, listname, dictionary):
    #     if self.debug:
    #         print('update_settings()')
    #     for key in dictionary.keys():
    #         print(key)
    #         for elem in self.tree.iterfind(listname):
    #             print(elem.get('key'))
    #             if elem.get('key') == key:
    #                 print(dictionary[key])
    #                 elem.set('value', str(dictionary[key]))
    #     return self.record()
    #
    # def record(self):
    #     return self.tree.write(self.file)
