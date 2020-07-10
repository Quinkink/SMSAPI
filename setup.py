# USE THIS COMMAND
# RUN >python setup.py bdist_msi
# decompyle3 -o path_for_save filename.pyc filename.pyc ...

from cx_Freeze import setup, Executable
import sys

current_version = '1.004'
status = 'BETA'

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
                     include_files=["data", "src", "ReadMe.txt", "LICENSE"],
                     excludes=["tcl", "asyncio", "concurrent", "ctypes", "distutils", "html",
                               "lib2to3", "logging", "test", "unittest", "xmlrpc"],
                     add_to_path=False,
                     include_msvcr=True,
                     optimize=2,
                     silent=True)

buildMSI_Options = dict(install_icon="src/app.ico",
                        target_name="SMSAPI-" + current_version,
                        initial_target_dir=r'[ProgramFilesFolder]\%s' % "SMSAPI",
                        product_code="SMSAPI-" + current_version,
                        upgrade_code="{59e50bd5-2592-43dd-abbe-50422457e001}",
                        all_users=False,
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

classifiers = [
    'Development Status :: ' + status + ' ' + current_version,
    'Environment :: Windows GUI',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Topic :: Communications :: SMS text'
]

setup(name='SMSAPI - send text message from desktop',
      version=current_version,
      author='Mark LEWIS',
      author_email='kingston.lewis@free.fr',
      url='https://github.com/Quinkink/SMSAPI',
      download_url='https://github.com/Quinkink/SMSAPI/releases',
      # about='A simple API interface for SMS',
      description='Send SMS via free.fr service provider API from Windows Desktop',
      long_description='This app is a way to make use of the free.fr SMS API.\
                        By editing the data/appSettings.xml file you can change the SMS target address.\
                        You never know you may be able to use this app for a different SMS API.',
      keywords=['sms', 'api', 'text', 'free.fr'],
      license='GNU GENERAL PUBLIC LICENSE',
      options=dict(build_exe=build_Options,
                   bdist_msi=buildMSI_Options),
      classifiers=classifiers,
      executables=executables)
