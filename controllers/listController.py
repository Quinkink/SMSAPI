# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\controllers\listController.py
# Compiled at: 2020-07-01 15:06:02
# Size of source mod 2**32: 5870 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk

class ListController(object):
    """
    ListController for ListView and ListModel
    """

    def __init__(self, app):
        """
        Init for ListController
        :param app: this is the main application controller
        """
        self.app = app
        self.app.lastView = 'List'
        self.debug = self.app.debug
        if self.debug:
            print('ListController __init__')
        self.messageValidError = ''
        self.model = self.app.model
        self.view = self.app.views['List']
        self.load_model_config()

    def load_model_config(self):
        """
        loads data to view
        :return: void
        """
        if self.debug:
            print('ListController:load_view_config()')
        self.view.listEnabled.delete(0, tk.END)
        for item in self.model.listboxEnabled_values:
            self.view.listEnabled.insert(tk.END, item)
        else:
            self.view.listDisabled.delete(0, tk.END)
            for item in self.model.listboxDisabled_values:
                self.view.listDisabled.insert(tk.END, item)
            else:
                self.view.labelEnabled.config(text=(self.model.strings['labelEnabled']), bg='WHITE', fg='GREEN')
                self.view.labelDisabled.config(text=(self.model.strings['labelDisabled']), bg='WHITE', fg='RED')
                self.view.addButton.config(text=(self.model.strings['buttonAdd']), command=(self.add))
                self.view.editButton.config(text=(self.model.strings['buttonEdit']), command=(self.edit))
                self.view.delButton.config(text=(self.model.strings['buttonDel']), command=(self.delete))
                self.application_feedback(self.model.strings['welcomeMessageList'])
                self.view.listEnabled.focus()

    def bind_view_buttons(self):
        """
        binds view buttons to controller methods
        :return: void
        """
        if self.debug:
            print('ListController:bind_view_buttons()')
        self.view.addButton.bind('<Button>', self.add)
        self.view.editButton.bind('<Button>', self.edit)
        self.view.delButton.bind('<Button>', self.delete)

    def add(self):
        """
        called when 'Add' button is pressed
        :return: void
        """
        if self.debug:
            print('listController:add()')
        self.app.show_view('Edit')

    def edit(self):
        """
        called when 'Edit' button is pressed
        :return: void
        """
        if self.debug:
            print('listController:edit()')
        if any((s.curselection() for s in (self.view.listEnabled, self.view.listDisabled))):
            if self.view.listEnabled.curselection():
                item = self.view.listEnabled.get(self.view.listEnabled.curselection()).strip()
            else:
                item = self.view.listDisabled.get(self.view.listDisabled.curselection()).strip()
            self.app.show_view('Edit', item)
        else:
            item = 'no list item selected'
            self.app.message_dialogue_error_feedback(self.model.strings['MessageTitleListSelectError'], self.model.strings['MessageListSelectError'])
            if self.debug:
                print(item)

    def delete(self):
        """
        called when 'Delete' button is pressed
        :return: void
        """
        if self.debug:
            print('listController:delete()')
        if any((s.curselection() for s in (self.view.listEnabled, self.view.listDisabled))):
            if self.view.listEnabled.curselection():
                item = self.view.listEnabled.get(self.view.listEnabled.curselection()).strip()
            else:
                item = self.view.listDisabled.get(self.view.listDisabled.curselection()).strip()
            if self.app.message_dialogue_user_confirm(self.model.strings['MessageTitleConfirmDelete'], self.model.strings['MessageConfirmDelete'] + item) == 'yes':
                self.model.xml_contacts.remove_from_list(item)
            self.app.show_view('List')
        else:
            item = 'no list item selected'
            self.app.message_dialogue_error_feedback(self.model.strings['MessageTitleListSelectError'], self.model.strings['MessageListSelectError'])
            if self.debug:
                print(item)

    def application_feedback(self, feedback, bgcolour='BLACK', fgcolour='WHITE'):
        """
        send feedback to user through view.feedback
        :param feedback: this is the message content
        :param bgcolour: background color defaults to WHITE
        :param fgcolour: foreground colour defaults to BLACK
        :return: void
        """
        if self.debug:
            print('application_feedback()')
            print('feedback : ' + feedback)
        self.view.feedback.config(state=(tk.NORMAL))
        self.view.feedback.delete(1.0, tk.END)
        self.view.feedback.config(background=bgcolour, foreground=fgcolour)
        self.view.feedback.insert(tk.END, feedback)
        self.view.feedback.config(state=(tk.DISABLED))