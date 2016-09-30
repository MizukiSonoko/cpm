#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
from color import *
__version__ = "0.0.1"

def init():
    pass

def status():
    pass

def install(name):
    print(bold(red(name)))
    print(yello(name))
    print(name)

def printHelp():
    print("usage: cpm \{init | install | status \} ")

def getOpt(argv):
    if len(argv) < 2:
        printHelp()
    elif argv[1] == "init":
        init()
    elif argv[1] == "status":
        status()
    elif argv[1] == "install" and len(argv) == 3 :
        install(argv[2])
    else:
        printHelp()

if __name__ == "__main__":
    getOpt(sys.argv)
