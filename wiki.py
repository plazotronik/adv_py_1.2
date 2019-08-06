#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import json


class WikiUrls:
    def __init__(self):
        if 'output' not in os.listdir():
            os.mkdir('output')
        self.path_out = os.path.join('output', 'wiki_urls.txt')
        self.api = "https://en.wikipedia.org/w/api.php"
        path_src = os.path.join('source', 'countries.json')
        file_src = open(path_src, mode='rt', encoding='utf8')
        self.data = json.load(file_src).__iter__()
        file_src.close()

    def __iter__(self):
        return self

    def __next__(self):
        country_name = self.data.__next__()["name"]["common"]
        params = {
            "action": "opensearch",
            "search": country_name,
            "format": "json"
        }
        resp = requests.get(url=self.api, params=params)
        country_url = resp.json()[3][0]
        txt = f'{country_name} - {country_url}'
        file_out = open(self.path_out, 'a', encoding='utf8')
        file_out.write(f'{txt}\n')
        file_out.close()
        return txt


if __name__ == '__main__':
    tmp = WikiUrls()
    for item in tmp:
        print(item)
