import unittest
from importlib import import_module
from doctest import DocTestSuite
from doctest import DocFileSuite
from sparc.testing.testlayer import SPARC_INTEGRATION_LAYER

class test_suite_mixin(object):
    package = 'define.to.dotted.package.being.tested'
    module = 'module_name_being_tested'
    layer = SPARC_INTEGRATION_LAYER # default
    
    def __new__(self):
        package = self.package
        module = self.module
        
        suite = unittest.TestSuite()
        try:
            docfiletest = DocFileSuite(module+'.txt',
                                                package=import_module(package))
            docfiletest.layer = self.layer
            suite.addTest(docfiletest)
        except IOError:
            pass # no docfile tests
        
        try:
            if module:
                doctest = DocTestSuite(package+'.'+module)
            else:
                doctest = DocTestSuite(package+'.'+module)
            doctest.layer = self.layer
            suite.addTest(doctest)
        except ValueError:
            pass # no doc tests
        return suite