#!/usr/bin/env python3
import socket
import argparse

def get_ip(hostname):
    """ Gets the IP address given a hostname.

    :param hostname: hostname
    :return: the ip of the host
    """
    try:
        return socket.gethostbyname(hostname)
    except:
        return "None"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('hostname', help='hostname to get the ip from')
    hostname = vars(parser.parse_args())['hostname']
    address = get_ip(hostname)
    print("The IP address of {} is {}".format(hostname, address))
