"""
Created on 17 Mar 2020

@author: Eleonore
"""
import tkinter as tk
import views.baseFrame as baseFrame


class AppView:
    """
    """

    def __init__(self, debug):
        """

        :param debug: (boolean)
        """
        self.debug = debug
        if self.debug:
            print('EditView __init__')

        """Load tkinter root"""
        # LOAD ROOT
        self.root = tk.Tk()
        # self.root.geometry('+300+160')
        self.root.resizable(0, 0)
        # self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.winfo_toplevel().wm_geometry("")
        self.root.pack_propagate(1)

        # WIDGETS
        """MAIN APP CONTAINER FRAME"""
        self.container = tk.Frame(self.root)
        self.menubar = None
        self.navigationmenu = None
        self.othermenu = None

        # GRID
        self.container.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.container.grid_columnconfigure(0, weight=1)
