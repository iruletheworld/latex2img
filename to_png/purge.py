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

list_files = os.listdir(os.getcwd())

list_files = [i for i in list_files if not i.endswith(('.bat', '.tex', '.py'))]

list_files = [os.path.join(os.getcwd(), i) for i in list_files]

for i in list_files:

    os.remove(i)

print('Purged!')
