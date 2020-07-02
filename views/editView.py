# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\views\editView.py
# Compiled at: 2020-06-30 17:27:40
# Size of source mod 2**32: 2179 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import views.baseFrame as baseFrame

class EditView(baseFrame.BaseFrame):
    """
    """

    def __init__(self, master, debug):
        super(EditView, self).__init__(master, debug)
        if self.debug:
            print('EditView __init__')
        self.enableVar = tk.StringVar()
        self.nameLabel = tk.Label(self, width=8, height=1, relief='groove', text='')
        self.userLabel = tk.Label(self, width=8, height=1, relief='groove', text='')
        self.codeLabel = tk.Label(self, width=8, height=1, relief='groove', text='')
        self.name = tk.Text(self, width=16, height=1)
        self.user = tk.Text(self, width=16, height=1)
        self.code = tk.Text(self, width=16, height=1)
        self.enable = tk.Checkbutton(self, text='', variable=(self.enableVar))
        self.cancelButton = tk.Button(self, width=0, text='')
        self.saveButton = tk.Button(self, width=0, text='')
        self.nameLabel.grid(row=1, column=0, columnspan=1, ipadx=0, ipady=0, padx=(2,
                                                                                   1), pady=2)
        self.userLabel.grid(row=2, column=0, columnspan=1, ipadx=0, ipady=0, padx=(2,
                                                                                   1), pady=2)
        self.codeLabel.grid(row=3, column=0, columnspan=1, ipadx=0, ipady=0, padx=(2,
                                                                                   1), pady=2)
        self.name.grid(row=1, column=1, columnspan=3, ipadx=0, ipady=0, padx=(1, 2), pady=2)
        self.user.grid(row=2, column=1, columnspan=3, ipadx=0, ipady=0, padx=(1, 2), pady=2)
        self.code.grid(row=3, column=1, columnspan=3, ipadx=0, ipady=0, padx=(1, 2), pady=2)
        self.enable.grid(row=4, column=2, columnspan=3, ipadx=0, ipady=0, padx=2, pady=0, sticky=(tk.EW))
        self.enable.grid_columnconfigure(0, weight=1)
        self.cancelButton.grid(row=5, column=0, columnspan=2, ipadx=0, ipady=0, padx=(2,
                                                                                      1), pady=2, sticky=(tk.EW))
        self.cancelButton.grid_columnconfigure(0, weight=1)
        self.saveButton.grid(row=5, column=2, columnspan=2, ipadx=0, ipady=0, padx=(1,
                                                                                    2), pady=2, sticky=(tk.EW))
        self.saveButton.grid_columnconfigure(0, weight=1)