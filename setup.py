import wx
import sys
import platform

APP = "main.py"
NAME = "RGB2HEX"
VERSION = "1.0.0.0"
AUTHOR = "Majiyd"
AUTHOR_EMAIL = "suleimanmajiyd@gmail.com"
URL = "https://minomall.com.ng"
LICENSE = "wxWidgets"
YEAR = "2018"

def buildApp():
    from distutils.core import setup
    try:
        import py2exe
    except ImportError:
        print('py2exe import failed')
        exit()

    archDat = platform.architecture()
    is32 = "32bit" in archDat
    bundle = 2 if is32 else 3
    OPTS = {
        "py2exe" : {
            "compressed" : True,
            "optimize" : 1,
            "bundle_files" : 1,
            "includes" : ["main"],
            "excludes": ["Tkinter", ],
            "dll_excludes": ["MSVCP90.dll", 'w9xpopen.exe']
        }
    }

    setup(name = NAME,
          version = VERSION,
          options = OPTS,
          windows = [{"script": APP,
                      "icon_resources": [(1, "r2h.ico")]
                      }],
          description = NAME,
          author = AUTHOR,
          author_email = AUTHOR_EMAIL,
          license = LICENSE,
          url = URL,
          zipfile=None,
          )

if __name__ == '__main__':
    if wx.Platform == '__WXMSW__':
        buildApp()