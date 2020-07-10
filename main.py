"""
Created on 17 Mar 2020

@author: Eleonore
"""

from controllers import application

filename = 'settings.xml'

if __name__ == '__main__':
    app = application.Application(filename)
    app.run()
