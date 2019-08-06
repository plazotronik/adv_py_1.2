#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def mdfive_string(path):
    with open(path, encoding='utf8') as file:
        for i in file:
            yield hashlib.md5(i.encode('utf8')).hexdigest()


if __name__ == '__main__':
    for i in mdfive_string('output/wiki_urls.txt'):
        print(i)
