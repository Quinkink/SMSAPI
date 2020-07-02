"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk


class BaseFrame(tk.Frame):
    """An abstract base class for the frames that sit inside PythonGUI.
    https://stackoverflow.com/questions/26213549/switching-between-frames-in-tkinter-menu

    Args:
      master (tk.Frame): The parent widget.
      controller (PythonGUI): The controlling Tk object.

    Attributes:
      controller (PythonGUI): The controlling Tk object.

    """

    def __init__(self, master, debug):
        tk.Frame.__init__(self, master)
        self.debug = debug
        self.grid()

        # WIDGETS
        self.feedback = tk.Text(self, width=0, height=1, state=tk.DISABLED)

        # GRID
        self.feedback.grid(row=0, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0, sticky=tk.EW)
        self.feedback.grid_columnconfigure(0, weight=1)
