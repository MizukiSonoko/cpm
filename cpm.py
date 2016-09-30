#! /usr/local/bin/python
# -*- coding: utf-8 -*-
import argparse
import sys
__version__ = "0.0.1"

def getOpt(argv):
    if len(argv) < 2:
        printHelp()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="This tool is ...(WIP)")
  parser.add_argument("-v", "--version", action='version', version='CPM '+__version__)
  parser.add_argument("install", nargs=2)
  args = parser.parse_args()
  print(args.install[1])
