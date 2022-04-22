#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""Dowloading data from an HTTP server"""
import os
import argparse
import logging
import timeit
import urllib.request
import http.client


# Cleaning terminal
os.system("clear")
# Setting the logging configurations
httpclient_logger = logging.getLogger("http.client")
logging.basicConfig(format='%(asctime)s - http-client.py - %(message)s', level=logging.DEBUG)


def httpclient_logging_patch(level=logging.DEBUG):
    """Enable HTTPConnection debug logging to the logging framework"""

    def httpclient_log(*args):
        httpclient_logger.log(level, " ".join(args))
        
    http.client.print = httpclient_log
    http.client.HTTPConnection.debuglevel = 1


# Get start time
starttime = timeit.default_timer()
logging.debug(f'Start time: {starttime}')

URL = 'https://www.github.com'
PROXY_ADDRESS = "165.24.10.8:8080"


if __name__ == "__main__":
    # Using http logging
    httpclient_logging_patch()
    # Request with proxy
    proxy = urllib.request.ProxyHandler({"http" : PROXY_ADDRESS})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(URL)
    logging.debug(f"Proxy server returns response headers: {resp.headers}")
    # Show the the time of script
    logging.debug(f'End time: {timeit.default_timer() - starttime}')