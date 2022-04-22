#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""Script for finding service name."""
import socket
import argparse


# Configuration of arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="get the service name", type=int)
parser.add_argument("--protocol", help="Set the protocol name", type=str)
args = parser.parse_args()


def find_service_name():
    protocolname = args.protocol
    port = args.port
    print(f"Port: {port} => Service name: {socket.getservbyport(port, protocolname)}")


if __name__ == '__main__':
    find_service_name()
