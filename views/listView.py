# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\Eleonore\Documents\PycharmProjects\SMSAPI\views\listView.py
# Compiled at: 2020-06-30 17:21:31
# Size of source mod 2**32: 2655 bytes
"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import views.baseFrame as baseFrame

class ListView(baseFrame.BaseFrame):
    """
    classdocs
    """

    def __init__(self, master, debug):
        super(ListView, self).__init__(master, debug)
        if self.debug:
            print('ListView __init__')
        self.labelEnabled = tk.Label(self, width=27, height=1, relief='flat', text='')
        self.labelDisabled = tk.Label(self, width=27, height=1, relief='flat', text='')
        scrollbarEnabled = tk.Scrollbar(self, orient=(tk.VERTICAL))
        self.listEnabled = tk.Listbox(self, width=30, height=3, yscrollcommand=(scrollbarEnabled.set),
          selectmode=(tk.BROWSE))
        scrollbarEnabled.config(command=(self.listEnabled.yview))
        scrollbarDisabled = tk.Scrollbar(self, orient=(tk.VERTICAL))
        self.listDisabled = tk.Listbox(self, width=30, height=3, yscrollcommand=(scrollbarDisabled.set),
          selectmode=(tk.BROWSE))
        scrollbarDisabled.config(command=(self.listDisabled.yview))
        self.addButton = tk.Button(self, width=0, text='')
        self.editButton = tk.Button(self, width=0, text='')
        self.delButton = tk.Button(self, width=0, text='')
        self.labelEnabled.grid(row=1, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0, sticky=(tk.EW))
        self.labelEnabled.grid_columnconfigure(0, weight=1)
        scrollbarEnabled.grid(row=2, column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, sticky=(tk.NS))
        self.listEnabled.grid(row=2, column=0, columnspan=5, ipadx=4, ipady=0, padx=2, pady=2)
        self.labelDisabled.grid(row=3, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0, sticky=(tk.EW))
        self.labelDisabled.grid_columnconfigure(0, weight=1)
        scrollbarDisabled.grid(row=4, column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, sticky=(tk.NS))
        self.listDisabled.grid(row=4, column=0, columnspan=5, ipadx=4, ipady=0, padx=2, pady=2)
        self.addButton.grid(row=5, column=0, columnspan=2, ipadx=0, ipady=0, padx=2, pady=2, sticky=(tk.EW))
        self.addButton.grid_columnconfigure(0, weight=1)
        self.editButton.grid(row=5, column=2, columnspan=2, ipadx=0, ipady=0, padx=0, pady=2, sticky=(tk.EW))
        self.editButton.grid_columnconfigure(0, weight=1)
        self.delButton.grid(row=5, column=4, columnspan=2, ipadx=0, ipady=0, padx=2, pady=2, sticky=(tk.EW))
        self.delButton.grid_columnconfigure(0, weight=1)