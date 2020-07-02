"""
Created on 17 Mar 2020

@author: Eleonore
"""

from controllers import application

filename = 'appStrings.xml'
debug = True

if __name__ == '__main__':
    app = application.Application(filename, debug)
    app.run()
