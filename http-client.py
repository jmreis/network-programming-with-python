#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""Dowloading data from an HTTP server"""
import os
import argparse
import logging
import timeit
import urllib.request
import http.client

# Default host server
REMOTE_SERVER_HOST = "https://www.python.org"

# Cleaning terminal
os.system("clear")
# Setting the logging configurations
httpclient_logger = logging.getLogger("http.client")
logging.basicConfig(format='%(asctime)s - http-client.py - %(message)s', level=logging.DEBUG)



def httpclient_logging(level=logging.DEBUG):
    """Enable HTTPConnection debug logging to the logging framework"""

    def httpclient_log(*args):
        httpclient_logger.log(level, " ".join(args))
        
    http.client.print = httpclient_log
    http.client.HTTPConnection.debuglevel = 1


# Get start time
starttime = timeit.default_timer()
logging.debug(f'Start time: {starttime}')


class HTTPClient:
    """Class for implementation of
    the http conection.
    """

    def __init__(self, host):
        self.host = host
    
    def get_data_from_host(self):
        """This function make a http request
        with the urlopen method from urllib, from 
        get the data from http server.

        Returns:
            str: return the page content.
        """
        request_data = urllib.request.urlopen(self.host)
        data = request_data.read()
        #text = data.decode('utf-8')
        return data


if __name__ == "__main__":
    # Using http logging
    httpclient_logging()

    # Setting the arguments
    parser = argparse.ArgumentParser(description="HTTP client example")
    parser.add_argument("--host", action="store",
     help="host url", 
     dest="host", default=REMOTE_SERVER_HOST)
    given_args = parser.parse_args()
    host = given_args.host

    # Using the class and get data from host
    client = HTTPClient(host)
    logging.debug(client.get_data_from_host())

    # Show the the time of script
    logging.debug(f'End time: {timeit.default_timer() - starttime}')