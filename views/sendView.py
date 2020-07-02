# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\views\sendView.py
# Compiled at: 2020-06-30 17:38:02
# Size of source mod 2**32: 1417 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import views.baseFrame as baseFrame
from tkinter import StringVar

class SendView(baseFrame.BaseFrame):
    """
    """

    def __init__(self, master, debug):
        super(SendView, self).__init__(master, debug)
        if self.debug:
            print('SendView __init__')
        self.selectedContact = StringVar()
        self.contacts = tk.Spinbox(self, width=30, textvariable=(self.selectedContact), state='readonly')
        self.message = tk.Text(self, width=24, height=7)
        self.clearButton = tk.Button(self, width=0, text='')
        self.sendButton = tk.Button(self, width=0, text='')
        self.contacts.grid(row=1, column=0, columnspan=2, ipadx=0, ipady=2, padx=2, pady=2, sticky=(tk.EW))
        self.contacts.grid_columnconfigure(0, weight=1)
        self.message.grid(row=2, column=0, columnspan=2, ipadx=0, ipady=0, padx=2, pady=0, sticky=(tk.EW))
        self.message.grid_columnconfigure(0, weight=1)
        self.clearButton.grid(row=3, column=0, ipadx=0, ipady=0, padx=4, pady=2, sticky=(tk.EW))
        self.clearButton.grid_columnconfigure(0, weight=1)
        self.sendButton.grid(row=3, column=1, ipadx=0, ipady=0, padx=4, pady=2, sticky=(tk.EW))
        self.sendButton.grid_columnconfigure(0, weight=1)