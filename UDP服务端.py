#coding:utf-8

import socket

target_host = '127.0.0.1'
target_port = 24000

buffer_size = 1024

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((target_host, target_port))

while True:
    print 'wating for message...'
    data, addr = udp_server.recvfrom(buffer_size)
    print 'Received from and return to:' + str(addr) + ':' + str(data)
    udp_server.sendto('ack', (addr[0], addr[1]))
udp_server.close()



