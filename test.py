#!/usr/bin/env python
# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, 'logs')

#base_dir = os.path.dirname(BASE_DIR)
#print "base dir is :%s" % base_dir
print "base dir is : %s" % BASE_DIR
print "log dir is: %s" % LOG_PATH

