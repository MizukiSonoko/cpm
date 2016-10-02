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

def generate():
    # Replace requests
    f =  open('CMakeLists.template', 'r')
    template = f.read()
    f.close()
    f = open('package.json', 'r')
    data = json.load(f)
    f.close()
    template = template.replace("@project_name", data["name"])
    lib_dirs = "lib/"
    inc_dirs = "lib/"
    libs     = ""
    for lib in data["libraries"]:
        inc_dirs += "{}/{}\n".format(lib["name"],lib["include"])
        lib_dirs += "{}/{}\n".format(lib["name"],lib["static"]["directory"])
        libs     += "{}\n".format(lib["name"],lib["static"]["name"])

    template = template.replace("@include_directories", inc_dirs)
    template = template.replace("@link_directories", lib_dirs)
    template = template.replace("@link_libraries", libs)

    if "sources" in data:
        srcs     = ""
        for src in data["sources"]:
            srcs     += "{}\n".format(src)
        template = template.replace("//ToDo_write", srcs)

    if "CXX_version" in data:
        template = template.replace('"-Wall"', '"-Wall -std={}"'.format(data["CXX_version"]))

    if "target" in data:
        template = template.replace("@target_name", data["target"])
    else:
        template = template.replace("@target_name", data["name"])

    with open('CMakeLists.txt', 'w') as fw:
        fw.write(template)



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
    elif argv[1] == "generate":
        generate()
    elif argv[1] == "install" and len(argv) == 3 :
        install(argv[2])
    else:
        printHelp()

if __name__ == "__main__":
    getOpt(sys.argv)
