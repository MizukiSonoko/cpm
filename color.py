# -*- coding: utf-8 -*-

def cyan(msg):
    return '\033[96m'+msg+'\033[0m'

def magenta(msg):
    return '\033[95m'+msg+'\033[0m'

def blue(msg):
    return '\033[94m'+msg+'\033[0m'

def yello(msg):
    return '\033[93m'+msg+'\033[0m'

def green(msg):
    return '\033[92m'+msg+'\033[0m'

def red(msg):
    return  '\033[91m'+msg+'\033[0m'

def bold(msg):
    return '\033[1m'+msg+'\033[0m'

def default(msg):
    return '\033[0m'+msg+'\033[0m'
