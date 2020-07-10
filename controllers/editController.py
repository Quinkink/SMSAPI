"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk


class EditController(object):
    """
    EditController for EditView and EditModel
    """

    def __init__(self, app):
        """
        Init for EditController
        :param app: this is the main application controller
        """
        self.app = app
        self.debug = self.app.debug
        if self.debug:
            print('EditController:__init__')
        self.messageValidError = ''
        self.model = self.app.model
        self.view = self.app.views['Edit']
        self.load_view_config()

    def load_view_config(self):
        """
        loads data to view
        :return: void
        """
        if self.debug:
            print('EditController:load_view_config()')
        self.view.nameLabel.config(text=(self.model.strings['labelName']))
        self.view.userLabel.config(text=(self.model.strings['labelUser']))
        self.view.codeLabel.config(text=(self.model.strings['labelCode']))
        self.view.name.insert(tk.END, self.model.contact['name'])
        self.view.user.insert(tk.END, self.model.contact['user'])
        self.view.code.insert(tk.END, self.model.contact['code'])
        self.view.enable.config(text=(self.model.strings['labelEnable']),
                                state=tk.NORMAL,
                                onvalue='True',
                                offvalue='False')
        self.view.enableVar.set(self.model.contact['enable'])
        self.view.cancelButton.config(text=(self.model.strings['buttonCancel']), command=self.cancel)
        self.view.saveButton.config(text=(self.model.strings['buttonSave']), command=self.save)
        self.application_feedback(self.model.strings['welcomeMessageEdit'])

    def save(self):
        """
        checks data from view and adds contact to XML file via model and handler
        :return: void
        """
        if self.debug:
            print('EditController:save()')
        feedback_background = 'RED'
        edit = False
        self.model.contact['name'] = self.view.name.get('1.0', tk.END).strip()
        self.model.contact['user'] = self.view.user.get('1.0', tk.END).strip()
        self.model.contact['code'] = self.view.code.get('1.0', tk.END).strip()
        self.model.contact['enable'] = self.view.enableVar.get()
        if self.model.contact['id'] != '':
            edit = True
        if not self.validate_name(edit):
            return_message = self.model.strings['ContactNameError'] + self.model.settings['maxNameLength']
        elif not self.validate_user():
            return_message = self.model.strings['ContactUserError'] + self.model.settings['defaultUserLength']
        elif not self.validate_code():
            return_message = self.model.strings['ContactCodeError'] + self.model.settings['defaultCodeLength']
        else:
            self.view.saveButton.config(state=tk.DISABLED)
            self.view.name.config(state=tk.DISABLED)
            self.view.user.config(state=tk.DISABLED)
            self.view.code.config(state=tk.DISABLED)
            self.view.enable.config(state=tk.DISABLED)
            if not self.add_contact_to_xml():
                return_message = self.model.strings['ContactNotAddedError']
            else:
                feedback_background = 'GREEN'
                if edit:
                    return_message = self.model.strings['ContactEditedSuccess']
                else:
                    return_message = self.model.strings['ContactAddedSuccess']
                self.view.cancelButton.config(text=(self.model.strings['buttonBack']), command=self.cancel)
                self.application_feedback(return_message, feedback_background)
        self.application_feedback(return_message, feedback_background)

    def application_feedback(self, feedback, bgcolour='BLACK', fgcolour='WHITE'):
        """
        send feedback to user through view.feedback
        :param feedback: this is the message content
        :param bgcolour: background color defaults to WHITE
        :param fgcolour: foreground colour defaults to BLACK
        :return: void
        """
        if self.debug:
            print('EditController:application_feedback()')
            print('feedback : ' + feedback)
        self.view.feedback.config(state=tk.NORMAL)
        self.view.feedback.delete(1.0, tk.END)
        self.view.feedback.config(background=bgcolour, foreground=fgcolour)
        self.view.feedback.insert(tk.END, feedback)
        self.view.feedback.config(state=tk.DISABLED)
        return True

    def add_contact_to_xml(self):
        """
        asks handler via model to add contact to XML file
        :return: the result from handler via model
        """
        if self.debug:
            print('EditController:add_contact_to_xml()')
            print(self.view.name.get('1.0', tk.END))
            print(self.view.user.get('1.0', tk.END))
            print(self.view.code.get('1.0', tk.END))
            print(self.view.enableVar.get())
        return self.model.save_contact(self.model.contact)

    def cancel(self):
        """
        called when CANCEL button is pressed
        :return: void
        """
        if self.debug:
            print('EditController:cancel()')
        self.view.saveButton.config(state=tk.NORMAL)
        self.view.name.config(state=tk.NORMAL)
        self.view.user.config(state=tk.NORMAL)
        self.view.code.config(state=tk.NORMAL)
        self.view.enable.config(state=tk.NORMAL)
        self.application_feedback(self.model.strings['welcomeMessageEdit'])
        self.view.name.delete(1.0, tk.END)
        self.view.user.delete(1.0, tk.END)
        self.view.code.delete(1.0, tk.END)
        self.view.enableVar.set(self.model.settings['defaultContactEnable'])
        self.app.show_view(self.app.lastView)

    def validate_name(self, edit):
        """
        validates user input 'name'
        :return: boolean
        """
        if self.debug:
            print('EditController: validate_name()')
            print(len(self.model.contact['name'].strip()))
        validation = True
        if not len(self.model.contact['name'].strip()) < 1:
            if len(self.model.contact['name'].strip()) > int(self.model.settings['maxNameLength']):
                validation = False
            if self.model.xml_contacts.get_element('contact', 'name', self.model.contact['name']) is not False:
                if edit is not True:
                    validation = False
            return validation

    def validate_user(self):
        """
        validates user input 'user'
        :return: boolean
        """
        if self.debug:
            print('EditController: validate_user()')
            print(len(self.model.contact['user'].strip()))
        validation = True
        if len(self.model.contact['user'].strip()) != int(self.model.settings['defaultUserLength']):
            validation = False
        return validation

    def validate_code(self):
        """
        validates user input 'code' (or 'pass' in XML file)
        :return: boolean
        """
        if self.debug:
            print('EditController: validate_code()')
            print(len(self.model.contact['code'].strip()))
        validation = True
        if len(self.model.contact['code'].strip()) != int(self.model.settings['defaultCodeLength']):
            validation = False
        return validation
