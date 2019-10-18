# -*- coding: utf-8 -*-

'''
Purge everything but *.bat, *.tex, *.py, *.md, the .git dir, the .vscode dir,
the docs dir.

Also purge the empty folders.

Written for Python 3.

Change Log
----------------------

* **Notable changes:**

    + Version : 1.0.1
        - Also purge empty folders.

    + Version : 1.0.0
        - First version.

'''

import os

__author__  = u'高斯羽 博士 (Dr. Gāo, Sī Yǔ)'
__version__ = '1.0.1'
__date__    = '2019-10-16'

tup_ignore = ('.bat', '.tex', '.py', '.gitignore', '.md')

list_files = []

# delete files
for root, dirnames, filenames in os.walk(os.getcwd()):

    for filename in filenames:

        list_files.append(os.path.join(root, filename))

list_files = [i for i in list_files if r'.git' not in i]
list_files = [i for i in list_files if r'.vscode' not in i]
list_files = [i for i in list_files if r'docs' not in i]

list_files = [i for i in list_files if not i.endswith(tup_ignore)]

for i in list_files:

    try:

        os.remove(i)

    except Exception as e:

        print(repr(e))

        pass

list_dirs = []

# delete empty folders
for root, dirnames, filenames in os.walk(os.getcwd()):

    for folder in dirnames:

        str_path_temp = os.path.join(root, folder)

        list_dirs.append(str_path_temp)

list_dirs = [i for i in list_dirs if r'.git' not in i]
list_dirs = [i for i in list_dirs if r'.vscode' not in i]
list_dirs = [i for i in list_dirs if r'docs' not in i]

for i in list_dirs:

    if not os.listdir(i):

        try:

            os.rmdir(i)

        except Exception as e:

            print(repr(e))

            pass

print('Purged!')
