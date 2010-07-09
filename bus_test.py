#!/usr/bin/env python

import sys
import time
from PyQt4 import QtGui
import qt4reactor
app = QtGui.QApplication(sys.argv)
qt4reactor.install()

def test_function(a, b):
    res = a + b
    print res

def second_function(a, b):
    print "I've been called with a = %s and b = %s" % (a, b)

from twisted.internet import reactor

reactor.bus.subscribe('test_function(int, int)', test_function)
reactor.bus.subscribe('test_function(int, int)', second_function)

reactor.runReturn()

time.sleep(1)
reactor.bus.emit('test_function(int, int)', 1, 2)

time.sleep(2)
reactor.stop()
