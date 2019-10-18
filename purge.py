# -*- coding: utf-8 -*-

'''
Purge everything but *.bat, *.tex, *.py, *.md, the .git dir, the .vscode dir,
the docs dir, the workflow_pics dir.

Also purge the empty folders.

Written for Python 3.

Change Log
----------------------

* **Notable changes:**

    + Version : 1.0.2
        - Removed hardcoding of folders to ignore.

    + Version : 1.0.1
        - Also purge empty folders.

    + Version : 1.0.0
        - First version.

'''

import os

__author__  = u'高斯羽 博士 (Dr. Gāo, Sī Yǔ)'
__version__ = '1.0.2'
__date__    = '2019-10-18'

tup_file_ignore = ('.bat', '.tex', '.py', '.gitignore', '.md')

tup_dir_ignore = ('.git', '.vscode', 'docs', 'workflow_pics')

list_files = []

# delete files
for root, dirnames, filenames in os.walk(os.getcwd()):

    for filename in filenames:

        list_files.append(os.path.join(root, filename))

for i in tup_dir_ignore:

    list_files = [j for j in list_files if i not in j]

list_files = [i for i in list_files if not i.endswith(tup_file_ignore)]

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

for i in tup_dir_ignore:

    list_dirs = [j for j in list_dirs if i not in j]

for i in list_dirs:

    if not os.listdir(i):

        try:

            os.rmdir(i)

        except Exception as e:

            print(repr(e))

            pass

print('Purged!')
