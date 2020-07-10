import xml.etree.ElementTree as ElementTree


class XMLStringsHandler(object):
    """

    """
    def __init__(self, file, debug=True):
        """

        :param file:
        :param debug:
        """
        self.debug = debug
        if self.debug:
            print('XMLStringsHandler: __init__')
        self.file = file
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
        if self.debug:
            print('root tag : ' + self.root.tag)
        
        # XML StringsFrame
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
    
    def get_dictionary(self, view):
        """

        :param view:
        :return:
        """
        # returns XML Strings file as a python dictionary (associative array)
        dictionary = {}
        for elem in self.tree.iterfind('view'):
            if self.debug:
                print(elem.get('frame'))
            if elem.get('frame') == view:
                if self.debug:
                    print('found ' + view)
                for child in elem.iter():
                    dictionary[child.get('key')] = child.get('value')
            if self.debug:
                print('XMLStringsHandler: dictionary')
                print(dictionary)
        return dictionary
