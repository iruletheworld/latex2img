# -*- coding: utf-8 -*-

'''
Purge everything but *.bat, *.tex, *.py

Change Log
----------------------

* **Notable changes:**
   + Version : 1.0.0
      - First version

'''

import os

__author__  = u'高斯羽 博士 (Dr. Gāo, Sī Yǔ)'
__version__ = '1.0.0'
__date__    = '2019-10-15'

list_files = []

for root, dirnames, filenames in os.walk(os.getcwd()):

    for filename in filenames:

        list_files.append(os.path.join(root, filename))

list_files = [i for i in list_files if not i.endswith(('.bat', '.tex', '.py'))]

list_files = [os.path.join(os.getcwd(), i) for i in list_files]

for i in list_files:

    try:

        os.remove(i)

    except Exception as e:

        print(repr(e))

        pass

print('Purged!')
