#!/usr/bin/python3

import py_compile
import os

py_compile.compile(os.environ['PYFILE'])
os.environ['PYFILEc']='main.pyc'
