#!/usr/bin/env python3
# For get network machine info
import socket
import argparse


# Configuration of arguments
parser = argparse.ArgumentParser()
parser.add_argument("--host", help="get the remote host", type=str)
args = parser.parse_args()


def show_remote_machine_info():
    """This function get the IP address of 
    the remote host.
    """
    remote_host = args.host

    try:
        print(f"IP address of {remote_host} is {socket.gethostbyname(remote_host)}")
    except socket.error as err_msg:
        print(f"{remote_host} {err_msg}")


if __name__ == "__main__":
    show_remote_machine_info()