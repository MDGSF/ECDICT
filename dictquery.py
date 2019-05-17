#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import sys
import time
import os
import io
import csv
import sqlite3
import codecs
import stardict

try:
    import json
except:
    import simplejson as json


def main():
    if len(sys.argv) < 2:
        print("Usage: dictquery.py {word}")
        return
    sqlitename = os.path.join(os.path.dirname(__file__), 'stardict.db')
    sd = stardict.StarDict(sqlitename, False)
    result = sd.query(sys.argv[1])
    if result is None:
        print("Can't find!!!")
        return
    print(result['word'])
    if len(result['definition']) > 0:
        print(result['definition'])
    if len(result['translation']) > 0:
        print(result['translation'])


if __name__ == "__main__":
    main()
