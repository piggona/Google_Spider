# date:2019/2/19
# -*- coding: utf-8 -*-
# auth：Haohao

from google_spider.magic_google.google import MagicGoogle
from google_spider.gog_spider.get_proxy import *
import pprint

def search_gog(query):
    proxies = get_proxy_val()
    print(proxies)
    mg = MagicGoogle(proxies)

    result = mg.search_page(query=query)
    for url in mg.search_url(query=query):
        pprint.pprint(url)

if __name__ == "__main__":
    search_gog("python")