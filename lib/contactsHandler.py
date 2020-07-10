import xml.etree.ElementTree as ElementTree
# noinspection PyUnresolvedReferences
import xml.dom.minidom as minidom


class XMLContactsHandler(object):

    def __init__(self, file, debug=True):
        self.debug = debug
        if self.debug:
            print('XMLContactsHandler: __init__')
        self.file = file
        self.tree = ElementTree.ElementTree(file=self.file)
        self.root = self.tree.getroot()
        if self.debug:
            print('root tag : ' + self.root.tag)

    def get_full_list(self, listname, key):
        """"""
        if self.debug:
            print('XMLContactsHandler: get_full_list()')
        codeList = ()
        for elem in self.tree.iterfind(listname):
            codeList += (elem.get(key),)
        else:
            return codeList

    def get_enable_list(self, listname, key):
        """"""
        if self.debug:
            print('XMLContactsHandler: get_enable_list()')
        codeList = ()
        for elem in self.tree.iterfind(listname):
            if elem.get('enable') == 'True':
                codeList += (elem.get(key),)
        else:
            return codeList

    def get_disable_list(self, listname, key):
        """"""
        if self.debug:
            print('XMLContactsHandler: get_enable_list()')
        codeList = ()
        for elem in self.tree.iterfind(listname):
            if elem.get('enable') == 'False':
                codeList += (elem.get(key),)
        else:
            return codeList

    def get_element(self, listname, key, value):
        """"""
        if self.debug:
            print('XMLContactsHandler: get_element()')
            print(listname + ' ' + key + ' ' + value)
        result = False
        for elem in self.tree.iterfind(listname):
            if self.debug:
                print(elem.get('name'))
            if elem.get(key) == value:
                result = {'id': elem.get('id'),
                          'name': elem.get('name'),
                          'user': elem.get('user'),
                          'code': elem.get('code'),
                          'enable': elem.get('enable')}
        else:
            return result

    def get_attribute(self, listname, key, zap):
        """"""
        if self.debug:
            print('XMLContactsHandler: get_attribute()')
        item = False
        for elem in self.tree.iterfind(listname):
            if elem.get('name') == key:
                item = elem.get(zap)
        else:
            return item

    def remove_from_list(self, name):
        """

        :param name: name of contact chosen in list view
        :return: returns result of record method
        """
        if self.debug:
            print('XMLContactsHandler: remove_from_list()')
            print('Attempting to remove: ' + name)
        for elem in self.root:
            elemName = elem.get('name')
            if elemName != name:
                print('not removing: ' + elemName)
            else:
                self.root.remove(elem)
                if self.debug:
                    print(name + ' was removed from list')

        # REGENERATE CONSECUTIVE ID'S
        i = 0
        for elem in self.root:
            elem.set('id', str(i))
            i += 1
        return self.record()

    def append_to_list(self, contact):
        """"""
        if self.debug:
            print('XMLContactsHandler: append_to_list()')
        if contact['id'] == '':
            contact['id'] = str(self.get_next_id())
            new_contact = ElementTree.Element('contact')
            for key in contact:
                new_contact.set(key, contact[key])
            else:
                ElementTree.Element.append(self.root, new_contact)

        else:
            pass
        for elem in self.root:
            if elem.get('id') == contact['id']:
                for key in contact:
                    elem.set(key, contact[key])

        else:
            if self.debug:
                print(ElementTree.tostring(self.root))
            return self.record()

    def get_next_id(self):
        """"""
        if self.debug:
            print('XMLContactsHandler: _next_id()')
        len(list(self.root))
        return len(list(self.root))

    def record(self):
        """
        This method takes the element tree and writes over the XML file with the new data
        :arg: None
        :return: True
        """
        if self.debug:
            print('XMLContactsHandler: record()')
            print(self.file)
        raw_str = ElementTree.tostring(self.root).strip()
        xml_str = '\n'.join([
            line for line in minidom.parseString(raw_str).toprettyxml(indent='  ').split('\n') if line.strip()])
        with open(self.file, 'wb') as f:
            f.write(xml_str.encode('utf-8'))
        return True
