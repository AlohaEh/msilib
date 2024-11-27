This is an msilib replacement for Python versions 3.13.0+
=========================================================

Usage
-----
This library can be import as either msilib or pymsilib.
I don't understand what is happening in the install with "import msilib".
It works as expected in a virtual environment but installing otherwise causes
an issue where it cannot find _msi. This can be fixed by either moving 
the _msi*.pyd directly into site-packages or change the first line in 
the __init__.py file (add a period):
        from ._msi import *

General
-------
MSILib is a python library for creating and manipulating MSI files.
This is legacy code. If you are creating a new project, I strongly suggest 
you do not use MSIs. 

Release Information
-------------------
MSILib has been deprecated for quite a while and as of Python 3.13.0, msilib 
is no longer included in the build.  This library takes the existing msilib 
code and packages it as an extra module.
The original code can be found in the Python Git repository (links below).
It is replicated here with minimal changes.

- Source code: https://github.com/TrevorHamm/msilib

- Original source code: 
         - https://github.com/python/cpython/tree/3.12/Lib/msilib
         - https://github.com/python/cpython/blob/3.12/PC/_msi.c
         - https://github.com/python/cpython/blob/3.12/PC/clinic/_msi.c.h


Copyright and License Information
---------------------------------

See the `LICENSE <https://github.com/python/cpython/blob/main/LICENSE>`_ for
information on the history of this software, terms & conditions for usage, and a
DISCLAIMER OF ALL WARRANTIES.

This distribution contains *no* GNU General Public License (GPL) code,
so it may be used in proprietary projects.

All trademarks referenced herein are property of their respective holders.
