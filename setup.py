# USE THIS COMMAND
# RUN >python setup.py bdist_msi
# decompyle3 -o path_for_save filename.pyc filename.pyc ...

from cx_Freeze import setup, Executable
import sys

# MSI shortcut table
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "SMSAPI",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]smsapi.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    ("ProgramMenuShortcut",  # Shortcut
     "ProgramMenuFolder",  # Directory_
     "SMSAPI",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]smsapi.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     ),

    # ===========================================================================
    # ("StartupShortcut",        # Shortcut
    #  "StartupFolder",          # Directory_
    #  "SMSAPI",                 # Name
    #  "TARGETDIR",              # Component_
    #  "[TARGETDIR]smsapi.exe",  # Target
    #  None,                     # Arguments
    #  None,                     # Description
    #  None,                     # Hotkey
    #  None,                     # Icon
    #  None,                     # IconIndex
    #  None,                     # ShowCmd
    #  'TARGETDIR'               # WkDir
    #  ),
    # ===========================================================================
]

msi_data = {"Shortcut": shortcut_table}

# Dependencies are automatically detected, but it might need
# fine tuning.
build_Options = dict(packages=["models", "controllers", "views", "lib"],
                     include_files=["data", "src", "ReadMe.txt"],
                     excludes=["tcl", "asyncio", "concurrent", "ctypes", "distutils", "html",
                               "lib2to3", "logging", "test", "unittest", "xmlrpc"],
                     add_to_path=False,
                     include_msvcr=True,
                     optimize=2,
                     silent=True)

buildMSI_Options = dict(install_icon="src/app.ico",
                        target_name="SMSAPI-1.002",
                        initial_target_dir=r'[ProgramFilesFolder]\%s' % "SMSAPI",
                        upgrade_code="{59e50bd5-2592-43dd-abbe-50422457e001}",
                        data=msi_data)
# product_code = "1125-4468-6442-5693"

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py',
               base=base,
               targetName='smsapi',
               icon="src/app.ico",
               copyright="Copyright (c) 2020")
]

setup(name='SMSAPI',
      version='1.002',
      author='kingston.lewis@free.fr',
      description='Send SMS via free.fr service provider API from Windows Desktop',
      options=dict(build_exe=build_Options,
                   bdist_msi=buildMSI_Options),
      executables=executables)
