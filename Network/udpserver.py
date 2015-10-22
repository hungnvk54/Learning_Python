#!/usr/bin/python
import socket
import sys

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)

server_address = ('192.168.4.200',7000)

tcpServer.bind(server_address)

print >>sys.stderr, '\nstarting on %s port %s' % server_address

while True:

	print >>sys.stderr, '\nwainting for new connectiong'

	datas , address = tcpServer.recvfrom(4096)

	print >>sys.stderr, '\nreceive connection from %s port %s' %(address)

	print >>sys.stderr, '\nreceive %d bytes from %s' % (len(datas),address)

	print >>sys.stderr, '\n%s' % datas

if data:
	send = tcpServer.sendTo(datas, address)
	print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)

