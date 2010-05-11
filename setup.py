#!/usr/bin/python

from distutils.core import setup, Extension

setup(name = 'PySVMLight',
      description = 'Interface to Thorsten Joachims\' SVM-Light',
      ext_modules = [
        Extension('PySVMLight',
                  include_dirs = ['lib/'],
                  sources = ['svmlight.c', 'lib/svm_learn_main.c', 'lib/svm_learn.c',
                             'lib/svm_common.c', 'lib/svm_hideo.c'])
      ])
