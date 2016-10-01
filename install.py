
from color import *

import requests
import json
import os
import subprocess

def install_library(name):
    data = fetch_json(name)
    if data:
        if download(data):
            if build(data):
                return data
    return None

def fetch_json(name):
    res = requests.get("https://raw.githubusercontent.com"+\
        "/MizukiSonoko/cpm/master/package/{}.json".format(name))
    if res.status_code == 200:
        print(blue("*****************************"+(len(name)*'*')))
        print(blue("OK!(^o^) Found \"{}\" !!".format(name)))
        print(blue("*****************************"+(len(name)*'*')))
        return res.json()
    elif res.status_code == 404:
        print(red("*****************************"+(len(name)*'*')))
        print(red("Sorry('A'`); Not found \"{}\" !!".format(name)))
        print(red("*****************************"+(len(name)*'*')))
        return None
    else:
        print(red("*****************************"+(len(name)*'*')))
        print(red("Sorry('A'`); Unknown \"{}\" !!".format(name)))
        print(red("*****************************"+(len(name)*'*')))
        return None

def download(data):
    if not os.path.exists(os.getcwd()+"/lib"):
        os.mkdir(os.getcwd()+"/lib")
    status = subprocess.check_call(
        ["git", "clone",
            data["url"], data["name"]
        ],cwd=os.getcwd()+"/lib")
    if status == 0:
        print(green("*******************************"))
        print(green("OK!(^o^)! Git clone success !!"))
        print(green("*******************************"))
        return True
    else:
        print(red("*******************************"))
        print(red("  Umm...('_')! clone failed... "))
        print(red("*******************************"))
        return False

def build(data):
    status = subprocess.check_call(
        data["build"].split(),
        cwd=os.getcwd()+"/lib/"+data["name"]
    )

def write(data):
    with open('package.json', 'rw') as f:
        package = json.load(f)
        package["libraries"].append({
              "name":"leveldb",
              "include":"include",
              "static":"out-static"
        })
        json.dump( package, f, sort_keys=True, indent=4)
