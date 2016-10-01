#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import os
import json

from color import *
from install import *
__version__ = "0.0.1"

def init():
    dic = {}
    dic["name"] = os.getcwd().split("/")[-1]
    dic["libraries"] = []
    with open('package.json', 'w') as f:
        json.dump(dic, f, sort_keys=True, indent=4)

def status():
    with open('package.json', 'r') as f:
        package = json.load(f)
        print("name: "+package["name"])
        for lib in package["libraries"]:
            print(lib["name"])


def install(name):
    print(bold(blue("=================")))
    print(bold(blue(" Install!! ")))
    print(bold(blue("=================")))
    data = install_library(name)

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
