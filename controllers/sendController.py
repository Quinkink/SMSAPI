"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import urllib.error
import urllib.request
from multiprocessing.pool import ThreadPool

import lib.functionEngine as functions


class SendController(object):
    """
    SendController for SendView and SendModel
    """

    def __init__(self, app):
        """
        Init for SendController
        :param app: this is the main application controller
        """
        self.app = app
        self.app.lastView = 'Send'
        self.debug = self.app.debug
        if self.debug:
            print('SendController __init__')
        self.messageValidError = ''
        self.model = self.app.model
        self.view = self.app.views['Send']
        self.load_model_config()

    def load_model_config(self):
        """
        loads data to view
        :return: void
        """
        if self.debug:
            print('SendController:load_view_config()')
        self.view.clearButton.config(text=(self.model.strings['buttonClear']), command=self.clear)
        self.view.sendButton.config(text=(self.model.strings['buttonSend']), command=self.send)
        self.view.contacts.config(values=self.model.spinbox_values)
        self.view.message.focus()
        self.application_feedback(self.model.strings['welcomeMessageSend'])

    def send(self):
        if self.debug:
            print('SendController: send()')
        feedback_background = 'RED'
        if not self.validate_contact():
            return_message = self.messageValidError
        elif not self.validate_message():
            return_message = self.messageValidError
        elif not self.internet_up():
            return_message = self.messageValidError
        else:
            self.view.contacts.config(state=tk.DISABLED)
            self.view.message.config(state=tk.DISABLED)
            self.view.sendButton.config(state=tk.DISABLED)
            self.view.clearButton.config(text=(self.model.strings['buttonReset']), command=self.clear)
            values = {'msg': self.model.message,
                      'pass': self.model.xml_contacts.get_attribute('contact', self.view.contacts.get(), 'code'),
                      'user': self.model.xml_contacts.get_attribute('contact', self.view.contacts.get(), 'user')}
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(functions.send, (self.model.settings['apiurl'], values, self.debug))
            self.application_feedback(self.model.strings['sendAttempt'], 'GREEN')
            if not async_result.get():
                return_message = self.model.strings['sendError']
            else:
                feedback_background = 'GREEN'
                return_message = self.model.strings['sendSuccess']
        self.application_feedback(return_message, feedback_background)
        self.view.clearButton.focus()

    def application_feedback(self, feedback, bgcolour='BLACK', fgcolour='WHITE'):
        """
        send feedback to user through view.feedback
        :param feedback: this is the message content
        :param bgcolour: background color defaults to WHITE
        :param fgcolour: foreground colour defaults to BLACK
        :return: void
        """
        if self.debug:
            print('SendController: application_feedback()')
            print('feedback : ' + feedback)
        self.view.feedback.config(state=tk.NORMAL)
        self.view.feedback.delete(1.0, tk.END)
        self.view.feedback.config(background=bgcolour, foreground=fgcolour)
        self.view.feedback.insert(tk.END, feedback)
        self.view.feedback.config(state=tk.DISABLED)

    def clear(self):
        """
        called when 'Clear' button is pressed
        :return: void
        """
        if self.debug:
            print('SendController: clear()')
        self.application_feedback(self.model.strings['welcomeMessageSend'])
        self.view.clearButton.config(text=(self.model.strings['buttonClear']), command=self.clear)
        self.view.sendButton.config(state=tk.NORMAL)
        self.view.contacts.config(state=tk.NORMAL)
        self.view.message.config(state=tk.NORMAL)
        if len(self.model.spinbox_values) > 1:
            self.view.selectedContact.set(self.model.strings['spinboxDefault'])
        else:
            self.view.selectedContact.set(self.model.strings['spinboxEmpty'])
        self.view.contacts.config(state='readonly')
        self.view.message.delete(1.0, tk.END)
        self.view.message.focus()

    def internet_up(self):
        if self.debug:
            print('InternetUp()')
            print('test url : ' + str(self.model.settings['internetupip']))
        req = urllib.request.Request(self.model.settings['internetupip'])
        try:
            response = urllib.request.urlopen(req, timeout=1)
            if self.debug:
                print('internetUp response code: ' + str(response.getcode()))
            return True
        except urllib.error.URLError as e:
            if self.debug:
                print(e.reason)
            self.messageValidError = self.model.feedback['InternetDownError']
        return False

    def validate_contact(self):
        """
        validates user input for contact in spinbox SELECTED and ENABLED
        :return: boolean
        """
        if self.debug:
            print('SendController:validate_contact()')
        validation = True
        if self.view.contacts.get() == self.model.strings['spinboxEmpty']:
            self.messageValidError = self.model.strings['emptyContactListError']
            validation = False
        if self.view.contacts.get() == self.model.strings['spinboxDefault']:
            self.messageValidError = self.model.strings['emptyContactError']
            validation = False
        if self.model.xml_contacts.get_attribute('contact', self.view.contacts.get(), 'enable') == str(False):
            self.messageValidError = self.model.strings['enabledContactError']
            validation = False
        if self.debug:
            print(self.messageValidError)
        return validation

    def validate_message(self):
        """
        validates user input 'message' for EMPTY or MAX LENGTH
        :return: boolean
        """
        if self.debug:
            print('SendController:validate_message()')
        self.model.message = self.view.message.get(1.0, tk.END + '-1c')
        if self.debug:
            print('message : [' + self.model.message + ']')
        validation = True
        if self.model.message == '':
            validation = False
            self.messageValidError = self.model.strings['emptyMessageError']
        elif len(self.model.message) > int(self.model.settings['maxMessageLength']):
            validation = False
            self.messageValidError = self.model.strings['longMessageError']
        return validation
