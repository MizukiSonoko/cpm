from __future__ import print_function
from color import *

import requests
import json
import os
import subprocess
import threading
import time

def install_library(name):
    data = fetch_json(name)
    if data:
        if download(data):
            if build(data):
                write(data)
                return data
    return None

def fetch_json(name):
    res = requests.get("https://raw.githubusercontent.com"+\
        "/MizukiSonoko/cpm/master/package/{}.json".format(name))
    if res.status_code == 200:
        print(green("- OK!(^o^) Found \"{}\" !!".format(name)))
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
        print(green("- OK!(^o^)! Git clone success !!"))
        return True
    else:
        print(red("*******************************"))
        print(red("  Umm...('_')! clone failed... "))
        print(red("*******************************"))
        return False

def build_thread(data):
    p = subprocess.Popen(
        data["build"],
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.getcwd()+"/lib/"+data["name"]
    )
    stdout, stderr = p.communicate()
    if p.returncode == 0:
        print(green("- OK!('v<)V build successfull !!"))
    else:
        print(red("Um... build failed"))
        print(red("---- log stdout ----"))
        print(stdout)
        print(red("---- log stderr ----"))
        print(stderr)

def build(data):
    print(green("- Build now !!"))
    th = threading.Thread(target=build_thread, args=(data,))
    th.setDaemon(True)
    th.start()
    while True:
        time.sleep(3)
        print('.', end="")
        if not th.isAlive():
            break
    return True

def write(data):
    with open('package.json', 'r') as f:
        package = json.load(f)
    package["libraries"].append({
        "name":data["name"],
        "include":data["include"],
        "static" :data["static"]
    })
    with open('package.json', 'w') as fw:
        json.dump( package, fw, sort_keys=True, indent=4)
