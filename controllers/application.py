"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
from tkinter import messagebox
import lib.tkErrorCatcher as tec
# APP MVC
from models.appModel import AppModel
from views.appView import AppView
# SEND MVC
from models.sendModel import SendModel
from views.sendView import SendView
from controllers.sendController import SendController
# EDIT MVC
from models.editModel import EditModel
from views.editView import EditView
from controllers.editController import EditController
# LIST MVC
from models.listModel import ListModel
from views.listView import ListView
from controllers.listController import ListController
# OTHER IMPORTS
import lib.functionEngine as functions


class Application(object):
    """
    The main application Controller
    Args: void
    """

    def __init__(self, settings):
        """
        Init for Application
        :param settings: (string) settings xml filename
        """
        self.appModel = AppModel(settings)
        self.debug = self.appModel.debug
        if self.debug:
            print('Application: __init__')
        tk.CallWrapper = tec.TkErrorCatcher
        self.appView = AppView(self.debug)
        self.appView.root.protocol('WM_DELETE_WINDOW', self.quit)
        self.appView.root.geometry(self.appModel.settings['geometryAppView'])
        self.visibleView = self.appModel.strings['defaultStartView']
        self.lastView = None
        self.app_mvc = {'Send': {'model': SendModel,  'view': SendView,
                                 'controller': SendController,
                                 'geometry': self.appModel.settings['geometrySendView']},
                        'Edit': {'model': EditModel,
                                 'view': EditView,
                                 'controller': EditController,
                                 'geometry': self.appModel.settings['geometryEditView']},
                        'List': {'model': ListModel,
                                 'view': ListView,
                                 'controller': ListController,
                                 'geometry': self.appModel.settings['geometryListView']}}
        self.model = None
        self.controller = None
        self.views = {}
        self.load_views()
        self.load_menu()

    def load_views(self):
        """
        loads all GUI views into list for view switching
        :return: void
        """
        if self.debug:
            print('Application: load_views')
        for name, mvc in self.app_mvc.items():
            frame = mvc['view'](self.appView.container, self.debug)
            frame.grid(row=2, column=2, sticky=(tk.NW + tk.SE))
            self.views[name] = frame
        else:
            self.show_view(self.visibleView)

    def show_view(self, mvc, contact_name=''):
        """
        shows selected view and load corresponding controller and model
        :param mvc: (sting) name of view
        :param contact_name: (string) contact name for edit
        :return: void
        """
        if self.debug:
            print('Application : show_view(' + mvc + ')')
            print('contact_name : ' + contact_name)
        filenames = {'settings': self.appModel.filenameSettings,
                     'contacts': self.appModel.filenameContacts,
                     'language': self.appModel.filenameLanguage}
        self.model = self.app_mvc[mvc]['model'](filenames, self.debug)
        if contact_name != '':
            self.model.load_contact(contact_name)
        self.controller = self.app_mvc[mvc]['controller'](self)
        self.views[mvc].tkraise()
        self.visibleView = mvc
        self.appView.root.update_idletasks()
        self.appView.root.geometry(self.app_mvc[mvc]['geometry'])
        try:
            self.load_menu()
        except AttributeError:
            pass

    def load_menu(self):
        """
        loads application top menu tk object and data. Should this be here or in appView?
        I guess here as I don't know a way to set command to controller methods from view menu
        :return: void
        """
        if self.debug:
            print('Application: load_menu()')
        self.appView.menubar = tk.Menu(self.appView.root)
        self.appView.othermenu = tk.Menu(self.appView.menubar, tearoff=0)
        if self.visibleView != 'Edit':
            if self.visibleView != 'Send':
                self.appView.menubar.add_command(label=(self.appModel.strings['menuSend']),
                                                 command=(lambda: self.show_view('Send')))
            if self.visibleView != 'List':
                self.appView.menubar.add_command(label=(self.appModel.strings['menuList']),
                                                 command=(lambda: self.show_view('List')))
            self.appView.othermenu.add_command(label=(self.appModel.strings['menuAbout']), command=self.about)
            self.appView.othermenu.add_command(label=(self.appModel.strings['menuHelp']), command=self.help)
            self.appView.othermenu.add_command(label=(self.appModel.strings['menuQuit']), command=self.quit)
            self.appView.menubar.add_cascade(label='Other', menu=self.appView.othermenu)
        self.appView.root.config(menu=self.appView.menubar)

    def help(self):
        """"""
        if self.debug:
            print('Application: help()')
        self.message_dialogue_information_feedback(self.appModel.strings['messageTitleHelp'],
                                                   self.appModel.strings['messageHelp'])

    def about(self):
        """"""
        if self.debug:
            print('Application: about()')
        self.message_dialogue_information_feedback(self.appModel.strings['messageTitleAbout'],
                                                   'Codded by Mark for a little fun'
                                                   '\non Github as Quinkink'
                                                   '\nkingston.lewis@free.fr')

    def run(self):
        """
        called by main. This is the main loop for tkinter
        :return: void
        """
        if self.debug:
            print('Application: run()')
        self.appView.root.title(self.appModel.strings['applicationTitle'])
        self.appView.root.iconbitmap(functions.find_data_file('app.ico', 'src'))
        self.appView.root.deiconify()
        self.appView.root.mainloop()

    def quit(self):
        """
        called by "Quit" button in menu
        :return: void
        """
        if self.debug:
            print('quit()')
        self.appView.root.destroy()

    def message_dialogue_warning_feedback(self, title, message, icon='warning'):
        """
        tkinter messagebox.showwarning GUI maybe this should be in the view...
        :param title: (string) the title of the message
        :param message: (string) message to display to user
        :param icon: (string) the choice of icon for messagebox: error, warning, information
        :return: void
        """
        if self.debug:
            print('ListController:message_dialogue_error_feedback()')
            print(message)
        tk.messagebox.showwarning(title, message, icon=icon)

    def message_dialogue_error_feedback(self, title, message, icon='error'):
        """
        tkinter messagebox.showerror GUI maybe this should be in the view...
        :param title: (string) the title of the message
        :param message: (string) message to display to user
        :param icon: (string) the choice of icon for messagebox: error, warning, information
        :return: void
        """
        if self.debug:
            print('ListController:message_dialogue_error_feedback()')
            print(message)
        tk.messagebox.showerror(title, message, icon=icon)

    def message_dialogue_information_feedback(self, title, message, icon='info'):
        """
        tkinter messagebox.showerror GUI maybe this should be in the view...
        :param title: (string) the title of the message
        :param message: (string) message to display to user
        :param icon: (string) the choice of icon for messagebox: error, warning, information
        :return: void
        """
        if self.debug:
            print('ListController:message_dialogue_error_feedback()')
            print(message)
        tk.messagebox.showinfo(title, message, icon=icon)

    def message_dialogue_user_confirm(self, title, message, icon='warning'):
        """
        tkinter messagebox.askquestion GUI maybe this should be in GUI
        :param title: (string) the title of the message
        :param message: (string) message to be displayed to user
        :param icon: icon to be displayed to user
        :return: boolean (YES,NO)
        """
        if self.debug:
            print('ListController: message_dialogue_user_confirm()')
            print(message)
        result = tk.messagebox.askquestion(title, message, icon=icon)
        return result
