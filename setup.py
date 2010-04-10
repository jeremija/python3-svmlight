from distutils.core import setup, Extension

setup(name = 'PySVMLight',
      description = 'Interface to Thorsten Joachims\' SVM-Light',
      ext_modules = [
        Extension('PySVMLight',
                  sources = ['PySVMLight.c', 'svm_learn_main.c', 'svm_learn.c',
                             'svm_common.c', 'svm_hideo.c'])
      ])
