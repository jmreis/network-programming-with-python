#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""Make a web server with python"""
import os
import sys
import argparse
import logging
import http.client
from http.server import BaseHTTPRequestHandler, HTTPServer

# Default host and port
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8800

# Cleaning terminal
os.system("clear")
# Setting the logging configurations
logging.basicConfig(format='%(asctime)s - http-server.py - %(message)s', level=logging.DEBUG)


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handler for the GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send msg to browser
        #self.wfile.write("The Server Works!!!")
        return


class CustomHTTPServer(HTTPServer):
    
    def __init__(self, host, port):
        server_address = (host, port)
        HTTPServer.__init__(self, server_address, RequestHandler)

    
def run_server(port):
    """This function is for run the simple
        http server.

    Args:
        port (int): number of port for run the http server
    """
    try:
        server = CustomHTTPServer(DEFAULT_HOST, port)
        logging.debug(f"HTTP server started on port: {port}")
        server.serve_forever()
    except Exception as err:
        logging.debug(f"Error: {err}")
    except KeyboardInterrupt:
        logging.debug("Server interrupted and is shutting down.....")
        server.socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP Server")
    parser.add_argument("--port", action="store", dest="port",
     type=int, default=DEFAULT_PORT)
    
    given_args = parser.parse_args()
    port = given_args.port
    run_server(port)