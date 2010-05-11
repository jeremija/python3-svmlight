#!/usr/bin/python

from distutils.core import setup, Extension

setup(name = 'svmlight',
      description = 'Interface to Thorsten Joachims\' SVM-Light',
      ext_modules = [
        Extension('svmlight',
                  include_dirs = ['lib/'],
                  sources = ['svmlight.c', 'lib/svm_learn_main.c', 'lib/svm_learn.c',
                             'lib/svm_common.c', 'lib/svm_hideo.c'])
      ])
