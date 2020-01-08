#!/usr/bin/python3

import os
import sys
import socket

def CheckOpenPorts(ip):
    port_range = range(1,65535)
    counter = 65535
    for port in port_range:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if s.connect_ex((ip,port)) == 0:
            counter -= 1
            print('Port ' + str(port) + ' is open')
    print('There are ' + str(counter) + ' ports closed')

def main():
    ip = input('Enter your ip address: ')
    if ip == "":
        print('You must enter an Ip address or url')
    else:
        CheckOpenPorts(ip)

if __name__ == "__main__":
    main()