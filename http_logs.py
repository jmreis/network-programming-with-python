#!/usr/bin/env python
# Script for testing http logs


import logging
import requests
import http.client

# Exemplo 1
logging.basicConfig(level=logging.DEBUG)
req = requests.get("http://ipinfo.io")
print(req.text)

# Exemplo 2
httpclient_logger = logging.getLogger("http.client")

def httpclient_logging_patch(level=logging.DEBUG):
    """Enable HTTPConnection debug logging to the logging framework"""

    def httpclient_log(*args):
        httpclient_logger.log(level, " ".join(args))

    # mask the print() built-in in the http.client module to use
    # logging instead
    http.client.print = httpclient_log
    # enable debugging
    http.client.HTTPConnection.debuglevel = 1

httpclient_logging_patch()
req = requests.get("http://ipinfo.io")
print(req.text)

# Requests com TOR
proxies = {'http':'socks5://127.0.0.1:9050', 'https':'socks5://127.0.0.1:9050'}
print(requests.get("http://ipinfo.io", proxies=proxies).text)
