#coding:utf-8

import socket

target_ip='127.0.0.1'
target_port=24000

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#发送一些数据,不用connect
client.sendto('hello this is udp',(target_ip,target_port))

#接受一些数据
data,addr=client.recvfrom(1024)

print data


